import axios from "axios";
import {API_URL} from "../Constants";


class UploadFilesService {
    upload(file, onUploadProgress) {
        let formData = new FormData();
        formData.append("file", file);
        return axios.post(`${API_URL}/upload`, formData, {
            headers: {
                "Content-Type": "multipart/form-data",
            },
            onUploadProgress,
        });
    }

    getFiles(){
        return axios.get(`${API_URL}/files`);
    }


    displayFile(filename) {
        return axios.get(`${API_URL}/files`)
    }

    download(filename) {
        console.log(`${API_URL}/files/${filename}`);
        return axios.get(`${API_URL}/files/${filename}`)
    }


}

export default new UploadFilesService();
