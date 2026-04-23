import {saveData} from '../Repositories/data.repository.js'

export const saveDataService=async(temperature,humidity)=>{
    try {
        await saveData(temperature,humidity)
    } catch (error) {
        console.log("Failed at save data.")
    }
}
