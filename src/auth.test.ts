import { hashPassword, comparePassword, generateToken } from './auth';

describe('auth', () => {
  it('should hash password correctly', () => {
    const password = 'password123';
    const hashedPassword = hashPassword(password);
    expect(bcrypt.compareSync(password, hashedPassword)).toBe(true);
  });

  it('should compare password correctly', () => {
    const password = 'password123';
    const hashedPassword = hashPassword(password);
    expect(comparePassword(password, hashedPassword)).toBe(true);
  });

  it('should generate token correctly', () => {
    const user = { name: 'John Doe', email: 'john.doe@example.com' };
    const token = generateToken(user);
    expect(token).not.toBe(null);
  });
});