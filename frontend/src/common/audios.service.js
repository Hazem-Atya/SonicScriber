import { API_URL } from './config.js'
import TokenService from './token.service'

export const AudioService = {

    headers: { "Authorization": "Token " + TokenService.getToken() },

    getAllAudios() {
        return fetch(API_URL + '/audios/', {
            headers: { "Authorization": "Token " + TokenService.getToken() },
        })
    }
    ,
    getAudioById(id) {
        return fetch(API_URL + '/audios/' + id, {
            headers: { "Authorization": "Token " + TokenService.getToken() },
        })

    },
    submitTranscription(transcription, audio_id) {
        const requestOptions = {
            method: "PATCH",
            body: JSON.stringify({ "transcription": transcription }),
            headers: {"Content-Type": "application/json", "Authorization": "Token " + TokenService.getToken() },

        };
        return fetch(`${API_URL}/audios/transcribe/${audio_id}`, requestOptions)
    }
}