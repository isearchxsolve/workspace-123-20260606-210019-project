import express, { Request, Response } from 'express';
import mongoose from 'mongoose';
import bcrypt from 'bcrypt';
import jwt from 'jsonwebtoken';

const app = express();
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

mongoose.connect('mongodb://localhost:27017/crm-app', { useNewUrlParser: true, useUnifiedTopology: true });

app.get('/', (req: Request, res: Response) => {
  res.send('CRM App');
});

app.listen(3000, () => {
  console.log('Server started on port 3000');
});