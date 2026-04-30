import * as dataRepository from '../Repositories/data.repository.js'

export const saveDataService=async(temperature,humidity)=>{
    try {
        await dataRepository.saveData(temperature,humidity)
    } catch (error) {
        console.error("Failed to service saveData",error)
    }
}

export const getDataService=async()=>{
   const data=await dataRepository.getData()
   try {
    if(data){
        return data
    }
    else{
        return ;
    }
   } catch (error) {
    console.log("Failed to service getData",error)
   }
}

export const getDataByIdService=async(id)=>{
    const data=await dataRepository.getDataById(id)
    try {
        if(data){
            return data
        }
        else{
            return ;
        }
    } catch (error) {
        console.error("Failed to service dataByid",error)
    }
}