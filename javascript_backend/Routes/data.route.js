import { Router } from "express";
import * as dataController from '../Controllers/data.controller.js'

const router=Router()

router.post("/data",dataController.saveDataController)
router.get("/data",dataController.getDataController)
router .get("/data/:id",dataController.getDataByIdController)
export default router