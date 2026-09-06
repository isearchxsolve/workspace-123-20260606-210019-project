import mongoose, { Document, Model, Schema } from 'mongoose';

interface UserDocument extends Document {
  name: string;
  email: string;
  password: string;
}

const userSchema = new Schema({
  name: String,
  email: String,
  password: String
});

const User = mongoose.model<UserDocument>('User', userSchema);

export default User;