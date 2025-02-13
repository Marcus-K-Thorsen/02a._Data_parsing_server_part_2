import express from 'express';
import parseTxt from '../parser_module/txtParser.js';

const router = express.Router();

router.get("/js", (req, res) => {
    res.send({ data: parseTxt() });
});

export default router;
