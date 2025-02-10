import express from 'express';
import parseYaml from '../parser_module/yamlParser.js';

const router = express.Router();

router.get("/yaml", (req, res) => {
    res.send({ data: parseYaml() });
});

export default router;
