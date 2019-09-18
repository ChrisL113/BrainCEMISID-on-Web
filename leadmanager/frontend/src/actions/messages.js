import { CREATE_MESSAGES, GET_ERRORS } from './types'

// CREATE MESSAGE
export const createMessage = msg =>{
    return {
        type: CREATE_MESSAGES,
        payload: msg
    }
}

// RETURN ERRORS
export const returnErrors = (msg, status) =>{
    return{
        type: GET_ERRORS,
        payload: { msg, status }
    }
}