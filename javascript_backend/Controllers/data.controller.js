import * as dataServices from '../Services/data.services.js'


export const saveDataController =async(req,res)=>{
    const {temperature,humidity}=req.body
    try {
        if(!temperature || !humidity){
            return res.status(400).json({message:"Temperature and humidity are required"})
        }
        const result=await dataServices.saveDataService(temperature,humidity)
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


export const getDataByIdController=async(req,res)=>{
    const id=req.params.id
    try {
        if(id){
            const data=await dataServices.getDataByIdService(id)
            if(data){
                return res.status(200).json({message:"Data retrieved successfully",data:data})
            }
            else{
                return res.status(404).json({message:"retrieve data failed"})
            }
        }
        else{
            return res.status(404).json({message:"Provide data id"})
        }
    } catch (error) {
        console.log("Error retrieving data in controller")
        res.status(500).json({message:"Internal server error"})
    }
}


export const updateDataByIdController=async(req,res)=>{
    const id=req.params.id
    const data_update=req.body
    console.log(data_update)

    try {
            if(id && data_update){
                const data=await dataServices.updateDataByIdService(id,data_update)
                if(data){
                    return res.status(200).json({message:"Data updated successfully",data:data})
                }
                else{
                    return res.status(400).json({message:"Failed to update data"})
                }
            }
            else{
                return res.status(400).json({message:"Provide valid data"})
            }
    } catch (error) {
        console.log("Error update data",error)
        res.status(500).json({message:"Internal server error"})
    }
}