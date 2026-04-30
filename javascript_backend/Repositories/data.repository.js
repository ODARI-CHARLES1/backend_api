import Data from "../Models/data.model.js";

export const saveData = async (temperature, humidity) => {
  try {
    const data = new Data({
      temperature,
      humidity
    });

    await data.save();

    console.log("Data saved successfully:", data);
    return data;

  } catch (error) {
    console.error("Error saving data:", error);
    throw error;
  }
};

export const getData=async()=>{
  try {
    const data=await Data.find();
    if(data){
      return data
      console.log("Data Retrieved successfully",data)
    }
    else{
      return ;
    }
    
  } catch (error) {
    console.error("Error retrieving data",error)
    throw error
  }
}

export const getDataById=async(id)=>{
  try {
    const data=await Data.findById(`${id}`)
    if(data){
      return data
    }
    else{
      return ;
    }
  } catch (error) {
    console.error(`Error retrieving data with id ${id}`,error)
    throw error
  }
}