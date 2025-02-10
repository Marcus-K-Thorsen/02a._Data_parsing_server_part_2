import express from 'express';
import parseJson from '../parser_module/jsonParser.js';

const router = express.Router();

router.get("/json", (req, res) => {
    res.send({ data: parseJson() });
});

export default router;
