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
        return axios.get(`${API_URL}/display/file/${filename}`)
    }

    stats(filename) {
        return axios.get(`${API_URL}/statistics/file/${filename}`)
    }


}

export default new UploadFilesService();
