import axios from "axios";
import {API_URL} from "../Constants";


class CsvWebService {

    /**
     * POST form data with a callback for tracking upload progress
     * @param file
     * @param onUploadProgress
     * @returns {Promise<AxiosResponse<T>>}
     */
    uploadCsvFile(file, onUploadProgress) {
        let formData = new FormData();
        formData.append("file", file);
        return axios.post(`${API_URL}/upload`, formData, {
            headers: {
                "Content-Type": "multipart/form-data",
            },
            onUploadProgress,
        });
    }

    /**
     * GET list of CSV files
     * @returns {Promise<AxiosResponse<T>>}
     */
    getCsvFiles(){
        return axios.get(`${API_URL}/files`);
    }

    /**
     * GET data list of the CSV file selected
     * @param filename
     * @returns {Promise<AxiosResponse<T>>}
     */
    displayCsvFile(filename) {
        return axios.get(`${API_URL}/display/file/${filename}`)
    }

    statsCsvFile(filename) {
        return axios.get(`${API_URL}/statistics/file/${filename}`)
    }


}

export default new CsvWebService();
