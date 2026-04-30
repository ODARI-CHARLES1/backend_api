import {saveDataService} from '../Services/data.services.js'


export const saveDataController =async(req,res)=>{
    const {temperature,humidity}=req.body
    try {
        if(!temperature || !humidity){
            return res.status(400).json({message:"Temperature and humidity are required"})
        }
        const result=await saveDataService(temperature,humidity)
        res.status(201).json({message:"Data saved successfully",data:result})
    } catch (error) {
        console.log("error saving data in controller")
        res.status(500).json({message:"Internal server error"})
    }
}


export const getDataController=async(req,res)=>{
    try {
        const data=await dataServices.getDataService() 
        if(data){
            return res.status(200).json({message:"Data retrieved successfully",data:data})
        }
        else{
            return res.status(404).json({message:"Retrieve data failed"})
        }
    } catch (error) {
        console.log("Error retrieving data in controller")
        res.status(500).json({message:"Internal server error"})
    }
}
