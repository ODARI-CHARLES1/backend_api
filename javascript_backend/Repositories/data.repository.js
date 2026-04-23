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

