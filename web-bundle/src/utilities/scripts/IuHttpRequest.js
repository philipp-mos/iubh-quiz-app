export class IuHttpRequest {

    static apiUrl = '/api/v1';


    /*
    * Get Results from IuQuiz-API-Call
    * @param {String} requestMethod - The Method you want to trigger, relative to apiUrl
    * @param {String} httpMethod - GET, PUT, POST, DELETE, etc.
    * @param {String} responseType - Default is json
    * @return {callback} callback
    */
    static getHttpRequest = (requestMethod, callback, httpMethod = 'GET', responseType = 'json') => {
        var xhr = new XMLHttpRequest();

        xhr.open(httpMethod, this.apiUrl + requestMethod, true);
        xhr.responseType = responseType;

        xhr.onload = () => {
            let responseStatus = xhr.status;

            if (responseStatus === 200) {
                callback(null, xhr.response);
            } 
            else {
                callback(responseStatus, xhr.response);
            }

        };

        xhr.send();
    }

}