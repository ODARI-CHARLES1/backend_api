import mongoose from 'mongoose'

const ConnectDB = async () => {
  try {
    await mongoose.connect(process.env.MONGO_URL, {
      serverApi: {
        version: '1',
        strict: true,
        deprecationErrors: true,
      },
    })
    console.log('DB connected successfully....')
  } catch (error) {
    console.error('Failed to connect to DB:', error)
    process.exit(1)
  }
}

export default ConnectDB
