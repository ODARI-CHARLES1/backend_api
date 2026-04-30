import mongoose from 'mongoose';

// add your connection string here and uncommnet const uri after pasting you connection string
//const uri=
const ConnectDB = async () => {
  try {
    const conn = await mongoose.connect(process.env.MONGODB_URI || uri );
    console.log(`MongoDB Connected: ${conn.connection.host}`);
  } catch (error) {
    console.error(`Error: ${error.message}`);
    process.exit(1);
  }
};

export default ConnectDB;
