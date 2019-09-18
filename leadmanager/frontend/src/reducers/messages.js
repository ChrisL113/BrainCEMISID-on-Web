import { CREATE_MESSAGES } from '../actions/types'

const initialState = {}

export default function(state = initialState, action){
    switch (action.type) {
        case CREATE_MESSAGES:
            return (state = action.payload)
        default:
            return state
    }
}