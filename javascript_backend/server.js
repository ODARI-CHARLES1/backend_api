import cors from 'cors'
import ConnectDB from './Config/mongodb.config.js'
import express from 'express'
import {config} from 'dotenv'

config()
const app=express()
app.use(cors())
app.use(express.json())

const PORT=process.env.PORT || 3000

app.get("/",(req,res)=>{
    res.send("Server running..")
})

ConnectDB();

app.listen(PORT,()=>console.log("Server runnning..."))