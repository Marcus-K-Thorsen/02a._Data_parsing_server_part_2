import express from 'express';
import parseXml from '../parser_module/xmlParser.js';

const router = express.Router();

router.get("/js", (req, res) => {
    res.send({ data: parseXml() });
});

export default router;
