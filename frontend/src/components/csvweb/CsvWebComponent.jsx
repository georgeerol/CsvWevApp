import React, {Component} from "react";
import {Column, Table} from "react-virtualized";
import 'react-virtualized/styles.css';
import CsvWebService from "../../service/CsvWebService"

const TABLE_TOTAL_WIDTH = 1900;
const TABLE_HEIGHT = 300;
const HEADER_HEIGHT = 20;
const ROW_HEIGHT = 30;

/**
 * This class is the CSV Web Application Component
 */
class CsvWebComponent extends Component {
    constructor(props) {
        super(props);
        this.chooseCsvFile = this.chooseCsvFile.bind(this);
        this.uploadClicked = this.uploadClicked.bind(this);
        this.displayClicked = this.displayClicked.bind(this);
        this.statsClicked = this.statsClicked.bind(this);


        this.state = {
            chosenCsvFiles: undefined,
            currentCsvFile: undefined,
            displayCsvData: undefined,
            statsCsvData: undefined,
            isDisplayActive: false,
            isStatsDisplayActive: false,
            progress: 0,
            message: "",
            fileData: [],

        };
    }

    componentDidMount() {
        CsvWebService.getCsvFiles().then((response) => {
            this.setState({
                fileData: response.data,
            });
        });
    }

    /**
     * Toggle on or off the provided csv file on the web page
     *
     */
    handleDisplayShow = () => {
        const {isDisplayActive} = this.state;
        this.setState({
            isDisplayActive: !isDisplayActive,
        })
    };
    /**
     * Toggle on or off the provided stats on the web page
     */
    handleStatsDisplayShow = () => {
        const {isStatsDisplayActive} = this.state;
        this.setState({
            isStatsDisplayActive: !isStatsDisplayActive,
        })
    };

    /**
     *  Fetch stats data and display them when the Data Statistics button is pressed
     * @param filename - the filename of stats data
     */
    statsClicked(filename) {
        console.log(filename);
        CsvWebService.statsCsvFile(filename).then(response => {
            this.setState({statsCsvData: response.data});
            console.log(this.state.statsCsvData)
        }).then(() => {
            this.handleStatsDisplayShow();
        }).catch(() => {
            this.setState({
                message: "Unable to display stats data"
            });
        });

    }

    /**
     * Fetch csv data and display them when the Display button is pressed
     * @param filename - the csv filename
     */
    displayClicked(filename) {
        console.log(filename);
        CsvWebService.displayCsvFile(filename).then(response => {
            this.setState({displayCsvData: response.data});

        }).then(() => {
            this.handleDisplayShow();
        }).catch(() => {
            this.setState({
                message: "Unable to display the csv data"
            });
        });

    }

    /**
     * Get the chosen csv file from the <type= 'file'> element.
     * @param event
     */
    chooseCsvFile(event) {
        this.setState({
            chosenCsvFiles: event.target.files,
        });
    }

    /**
     *  Upload the chosen file when the Upload button is clicked
     */
    uploadClicked() {
        // accessing the current csv file as the first data
        let currentFile = this.state.chosenCsvFiles[0];
        this.setState({
            progress: 0,
            currentCsvFile: currentFile,
        });

        CsvWebService.uploadCsvFile(currentFile, (event) => {
            this.setState({
                progress: Math.round((100 * event.loaded) / event.total),

            });
        })
            .then((response) => {
                this.setState({
                    message: response.data.message,
                });
                return CsvWebService.getCsvFiles();
            })
            .then((files) => {
                this.setState({
                    fileData: files.data,
                });
            })
            .catch(() => {
                this.setState({
                    progress: 0,
                    message: "Unable to upload the file! Make sure it's the right csv file.",
                    currentCsvFile: undefined,
                });
            });

        this.setState({
            chosenCsvFiles: undefined,
        });
    }


    render() {
        const {
            chosenCsvFiles,
            currentCsvFile,
            progress,
            message,
            fileData,
        } = this.state;


        return (

            <div>
                <h1> Csv Web Application </h1>
                <div className="container">
                    <label className="btn btn-default">
                        <input type="file" onChange={this.chooseCsvFile}/>
                    </label>

                    <button className="btn btn-success" disabled={!chosenCsvFiles} onClick={this.uploadClicked}>Upload
                    </button>

                    <div className="alert alert-light" role="alert">
                        {message}
                    </div>
                </div>

                <div className="container">
                    <div className="card-header">List of CSVs</div>
                    <table className="table">
                        <tbody>
                        {fileData &&
                        fileData.map((file, index) => (
                            <tr key={index}>
                                <td><a href={file.url}>{file.name}</a></td>
                                <td>
                                    <button className="btn btn-success" onClick={() => this.displayClicked(file.name)}>
                                        Display
                                    </button>
                                </td>
                                <td>
                                    <button className="btn btn-warning on" onClick={() => this.statsClicked(file.name)}>
                                        Date Statistics
                                    </button>
                                </td>
                            </tr>
                        ))}
                        </tbody>
                    </table>

                    {this.state.isStatsDisplayActive ?
                        <Table
                            width={TABLE_TOTAL_WIDTH / 8}
                            height={TABLE_HEIGHT}
                            headerHeight={HEADER_HEIGHT}
                            rowHeight={ROW_HEIGHT}
                            rowCount={this.state.statsCsvData.persons_per_year.length}
                            rowGetter={({index}) => this.state.statsCsvData.persons_per_year[index]}
                        >

                            <Column
                                dataKey="year"
                                label="Year"
                                width={TABLE_TOTAL_WIDTH / 8}
                            />

                            <Column
                                dataKey="person"
                                label="Person"
                                width={TABLE_TOTAL_WIDTH / 8}
                            />


                        </Table>
                        : null

                    }
                </div>
                <br></br>
                <br></br>
                <br></br>
                {this.state.isDisplayActive ?


                    <Table
                        width={TABLE_TOTAL_WIDTH}
                        height={TABLE_HEIGHT}
                        headerHeight={HEADER_HEIGHT}
                        rowHeight={ROW_HEIGHT}
                        rowCount={this.state.displayCsvData.csv_data.length}
                        rowGetter={({index}) => this.state.displayCsvData.csv_data[index]}
                    >
                        <Column
                            headerRenderer={this.headerRenderer}
                            dataKey="guid"
                            label="Guid"
                            width={2 * TABLE_TOTAL_WIDTH}
                        />

                        <Column
                            headerRenderer={this.headerRenderer}
                            dataKey="name"
                            label="Name"
                            width={TABLE_TOTAL_WIDTH / 2}
                        />

                        <Column
                            dataKey="first"
                            label="First"
                            width={TABLE_TOTAL_WIDTH / 2}
                        />

                        <Column
                            dataKey="last"
                            label="Last"
                            width={TABLE_TOTAL_WIDTH / 2}
                        />

                        <Column
                            dataKey="email"
                            label="Email"
                            width={TABLE_TOTAL_WIDTH}
                        />

                        <Column
                            dataKey="value"
                            label="Value"
                            width={TABLE_TOTAL_WIDTH / 3}
                        />

                        <Column
                            dataKey="date"
                            label="Date"
                            width={TABLE_TOTAL_WIDTH}
                        />

                        <Column
                            dataKey="phone"
                            label="Phone"
                            width={TABLE_TOTAL_WIDTH}
                        />


                        <Column
                            dataKey="age"
                            label="Age"
                            width={TABLE_TOTAL_WIDTH / 5}
                        />

                        <Column
                            dataKey="state"
                            label="State"
                            width={TABLE_TOTAL_WIDTH / 4}
                        />

                        <Column
                            dataKey="street"
                            label="Street"
                            width={TABLE_TOTAL_WIDTH}
                        />

                    </Table>
                    : null
                }
                <br></br>
                <br></br>
                <br></br>

                {currentCsvFile && (
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


export default CsvWebComponent;
