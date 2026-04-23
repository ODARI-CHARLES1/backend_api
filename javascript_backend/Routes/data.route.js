import { Router } from "express";
import {saveDataController} from '../Controllers/data.controller.js'

const router=Router()

router.post("/data",saveDataController)

export default router