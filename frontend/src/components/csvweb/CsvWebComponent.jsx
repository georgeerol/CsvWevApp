import React, {Component} from "react";
import UploadService from "../../service/UploadFilesService"


class CsvWebComponent extends Component {
    constructor(props) {
        super(props);
        this.selectFile = this.selectFile.bind(this);
        this.download = this.download.bind(this);
        this.upload = this.upload.bind(this);

        this.state = {
            selectedFiles: undefined,
            currentFile: undefined,
            progress: 0,
            message: "",

            fileInfos: [],
        };
    }

    componentDidMount() {
        UploadService.getFiles().then((response) => {
            this.setState({
                fileInfos: response.data,
            });
        });
    }

    selectFile(event) {
        this.setState({
            selectedFiles: event.target.files,
        });
    }

    download(filename) {
        console.log(filename);
        UploadService.download(filename).then(response => {
            console.log('george')
            console.log(response);
        });
    }

    upload() {
        let currentFile = this.state.selectedFiles[0];
        console.log('george');
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
                                    <button className="btn btn-success">
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

export default CsvWebComponent;
