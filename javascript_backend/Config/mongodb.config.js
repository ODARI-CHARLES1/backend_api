import mongoose from 'mongoose';
const uri="mongodb+srv://odaricharles23_db_user:1GDRwlP68mt42xbp@cluster0.dstbd8n.mongodb.net/?appName=Cluster0"
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
