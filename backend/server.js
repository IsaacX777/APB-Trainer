import { initialize, generateLXS, generateEO } from './generate-scramble.js';
import express from 'express';

const app = express();
const port = 8000;

await initialize();

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});

app.get('/lxs/:set/:id', (req, res) => {
  const { set, id } = req.params;

  const scramble = generateLXS(set, id);
  res.send(scramble);
});

app.get('/eo-pair/:set/:id', (req, res) => {
  const { set, id } = req.params;

  const scramble = generateEO(set, id);
  res.send(scramble);
});