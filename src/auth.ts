import bcrypt from 'bcrypt';
import jwt from 'jsonwebtoken';

const hashPassword = (password: string) => {
  const salt = bcrypt.genSaltSync(10);
  return bcrypt.hashSync(password, salt);
};

const comparePassword = (password: string, hashedPassword: string) => {
  return bcrypt.compareSync(password, hashedPassword);
};

const generateToken = (user: any) => {
  return jwt.sign({ user }, process.env.SECRET_KEY, { expiresIn: '1h' });
};

export { hashPassword, comparePassword, generateToken };