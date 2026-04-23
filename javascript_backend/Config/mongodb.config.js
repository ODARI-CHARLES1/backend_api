import mongoose from "mongoose"


export default ConnectDB=async()=>{
    const MONGO_URL=process.env.MONGO_URL
    try {
        await mongoose.connect(MONGO_URL)
        mongoose.connection.on("connected",()=>console.log("DB connected successfully"))
    } catch (error) {
        console.log("Failed to connect :",error)
    }
}