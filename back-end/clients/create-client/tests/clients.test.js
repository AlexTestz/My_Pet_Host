const request = require('supertest');
const app = require('../src/index');

describe('POST /api/clients', () => {
  it('should create a new client and return 201', async () => {
    const res = await request(app)
      .post('/api/clients')
      .send({
        name: 'Test',
        last_name: 'User',
        email: `test${Date.now()}@example.com`, // único cada vez
        phone: '123456789'
      });

    expect(res.statusCode).toBe(201);
    expect(res.body).toHaveProperty('client');
    expect(res.body.client).toHaveProperty('id');
  });
});
