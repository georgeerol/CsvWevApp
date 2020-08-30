import axios from "axios";

export default axios.create({
    baseURL: "http://localhost:5003/csvwebapp",
    headers: {
        "Content-type": "application/json"
    }
});
