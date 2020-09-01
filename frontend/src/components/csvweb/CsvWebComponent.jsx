import React, {Component} from "react";
import {Column, Table} from "react-virtualized";
import 'react-virtualized/styles.css'; // only needs to be imported once
import Draggable from "react-draggable";
import UploadService from "../../service/UploadFilesService"

const TOTAL_WIDTH = 1900;


class CsvWebComponent extends Component {
    constructor(props) {
        super(props);
        this.selectFile = this.selectFile.bind(this);
        this.upload = this.upload.bind(this);
        this.displayClicked = this.displayClicked.bind(this);
        this.getKeys = this.getKeys.bind(this);
        this.getHeader = this.getHeader.bind(this);
        this.getRowsData = this.getRowsData.bind(this);


        this.state = {
            selectedFiles: undefined,
            currentFile: undefined,
            display_csv_data: undefined,
            isDisplayActive: false,
            hasMore: true,
            progress: 0,
            message: "",
            fileInfos: [],

            widths: {
                name: 0.33,
                location: 0.33,
                description: 0.33
            }
        };
    }

    componentDidMount() {
        UploadService.getFiles().then((response) => {
            this.setState({
                fileInfos: response.data,
            });
        });
    }

    handleShow = () => {
        const {isDisplayActive} = this.state;
        this.setState({
            isDisplayActive: !isDisplayActive,
        })
    };

    displayClicked(filename) {
        console.log(filename);
        UploadService.displayFile(filename).then(response => {
            this.setState({display_csv_data: response.data});

        }).then(() => {
            this.handleShow();
            console.log("LALA LAND");
            console.log(this.state.display_csv_data.csv_data)
        }).catch(() => {

        });

    }

    getKeys = function () {
        console.log("Stephane");
        console.log(this.state.display_csv_data.csv_data[0]);
        return Object.keys(this.state.display_csv_data.csv_data[0]);
    };

    getHeader = function () {
        var keys = this.getKeys();
        return keys.map((key, index) => {
            return <th key={key}>{key.toUpperCase()}</th>
        })
    };

    getRowsData = function () {
        var items = this.state.display_csv_data.csv_data;
        var keys = this.getKeys();
        return items.map((row, index) => {
            return <tr key={index}><RenderRow key={index} data={row} keys={keys}/></tr>
        });
    };


    selectFile(event) {
        this.setState({
            selectedFiles: event.target.files,
        });
    }


    upload() {
        let currentFile = this.state.selectedFiles[0];
        this.setState({
            progress: 0,
            currentFile: currentFile,
        });

        UploadService.upload(currentFile, (event) => {
            this.setState({
                progress: Math.round((100 * event.loaded) / event.total),

            });
        })
            .then((response) => {
                this.setState({
                    message: response.data.message,
                });
                return UploadService.getFiles();
            })
            .then((files) => {
                this.setState({
                    fileInfos: files.data,
                });
            })
            .catch(() => {
                this.setState({
                    progress: 0,
                    message: "Could not upload the file!",
                    currentFile: undefined,
                });
            });

        this.setState({
            selectedFiles: undefined,
        });
    }


    render() {
        const {
            selectedFiles,
            currentFile,
            progress,
            message,
            widths,
            fileInfos,
        } = this.state;


        return (

            <div>
                <h1> Csv Web Application </h1>

                <label className="btn btn-default">
                    <input type="file" onChange={this.selectFile}/>
                </label>

                <button
                    className="btn btn-success"
                    disabled={!selectedFiles}
                    onClick={this.upload}
                >Upload
                </button>

                <div className="alert alert-light" role="alert">
                    {message}
                </div>

                <div className="container">
                    <div className="card-header">List of CSVs</div>
                    <table className="table">
                        <tbody>
                        {fileInfos &&
                        fileInfos.map((file, index) => (
                            <tr key={index}>
                                <td><a href={file.url}>{file.name}</a></td>
                                <td>
                                    <button className="btn btn-success" onClick={() => this.displayClicked(file.name)}>
                                        Display
                                    </button>
                                </td>
                                <td>
                                    <button className="btn btn-warning">
                                        Date Statistics
                                    </button>
                                </td>
                            </tr>
                        ))}
                        </tbody>
                    </table>

                </div>

                {this.state.isDisplayActive ?


                    <Table
                        width={TOTAL_WIDTH}
                        height={300}
                        headerHeight={20}
                        rowHeight={30}
                        rowCount={this.state.display_csv_data.csv_data.length}
                        rowGetter={({index}) => this.state.display_csv_data.csv_data[index]}
                    >
                        <Column
                            headerRenderer={this.headerRenderer}
                            dataKey="guid"
                            label="Guid"
                            width={2 * TOTAL_WIDTH}
                        />

                        <Column
                            headerRenderer={this.headerRenderer}
                            dataKey="name"
                            label="Name"
                            width={TOTAL_WIDTH/2}
                        />

                        <Column
                            dataKey="first"
                            label="First"
                            width={TOTAL_WIDTH/2}
                        />

                        <Column
                            dataKey="last"
                            label="Last"
                            width={TOTAL_WIDTH/2}
                        />

                        <Column
                            dataKey="email"
                            label="Email"
                            width={TOTAL_WIDTH}
                        />

                        <Column
                            dataKey="value"
                            label="Value"
                            width={TOTAL_WIDTH/3}
                        />

                        <Column
                            dataKey="date"
                            label="Date"
                            width={TOTAL_WIDTH}
                        />

                        <Column
                            dataKey="phone"
                            label="Phone"
                            width={TOTAL_WIDTH}
                        />

                        <Column
                            dataKey="age"
                            label="Age"
                            width={TOTAL_WIDTH/5}
                        />

                        <Column
                            dataKey="state"
                            label="State"
                            width={TOTAL_WIDTH/4}
                        />

                        <Column
                            dataKey="street"
                            label="Street"
                            width={TOTAL_WIDTH}
                        />


                    </Table>
                    : null
                }
                {currentFile && (
                    <div className="progress">
                        <div
                            className="progress-bar progress-bar-info progress-bar-striped"
                            role="progressbar"
                            aria-valuenow={progress}
                            aria-valuemin="0"
                            aria-valuemax="100"
                            style={{width: progress + "%"}}
                        >
                            {progress}%
                        </div>
                    </div>
                )}

            </div>
        );
    }

}

const RenderRow = (props) => {
    return props.keys.map((key, index) => {
        return <td key={props.data[key]}>{props.data[key]}</td>
    })
};

export default CsvWebComponent;
