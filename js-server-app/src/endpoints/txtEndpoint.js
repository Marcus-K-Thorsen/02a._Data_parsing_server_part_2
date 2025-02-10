import express from 'express';
import parseTxt from '../parser_module/txtParser.js';

const router = express.Router();

router.get("/txt", (req, res) => {
    res.send({ data: parseTxt() });
});

export default router;
