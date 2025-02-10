import express from 'express';
import parseCsv from '../parser_module/csvParser.js';

const router = express.Router();

router.get("/csv", (req, res) => {
    res.send({ data: parseCsv() });
});

export default router;
