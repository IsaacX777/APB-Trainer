import { initialize, generateLXS, generateEO } from './generate-scramble.js';
import express from 'express';
import cors from 'cors';

const app = express();
const port = 8000;

app.use(cors({
  origin: '*',
}));

await initialize();

app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});

app.get('/', (req, res) => {
  res.send('API for APB Trainer');
});

app.get('/lxs/:set/:id', (req, res) => {
  const { set, id } = req.params;

  const scramble = generateLXS(set, id);
  res.send(scramble);
});

app.get('/eo_pair/:set/:id', (req, res) => {
  const { set, id } = req.params;

  const scramble = generateEO(set, id);
  res.send(scramble);
});