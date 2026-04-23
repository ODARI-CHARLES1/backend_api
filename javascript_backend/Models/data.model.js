import mongoose from 'mongoose';

const dataSchema = new mongoose.Schema(
  {
    temperature: {
      type: Number,
      required: true
    },
    humidity: {
      type: Number,
      required: true
    }
  },
  {
    timestamps: true
  }
);

const Data = mongoose.model("Data", dataSchema);

export default Data;