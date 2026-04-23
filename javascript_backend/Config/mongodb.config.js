import { MongoClient, ServerApiVersion } from 'mongodb'
const uri = "mongodb://odaricharles23_db_user:h91l8A13gJhsmZU1@ac-wnmaehi-shard-00-00.ohvrfbr.mongodb.net:27017,ac-wnmaehi-shard-00-01.ohvrfbr.mongodb.net:27017,ac-wnmaehi-shard-00-02.ohvrfbr.mongodb.net:27017/?ssl=true&replicaSet=atlas-ys22an-shard-0&authSource=admin&appName=Cluster0";

// Create a MongoClient with a MongoClientOptions object to set the Stable API version
const client = new MongoClient(uri, {
  serverApi: {
    version: ServerApiVersion.v1,
    strict: true,
    deprecationErrors: true,
  }
});

const ConnectDB=async()=>{
  try {
    // Connect the client to the server	(optional starting in v4.7)
    await client.connect();
    // Send a ping to confirm a successful connection
    await client.db("admin").command({ ping: 1 });
    console.log("DB connected successfully....");
  } finally {
    // Ensures that the client will close when you finish/error
    await client.close();
  }
}

export default ConnectDB
