const OpenApiTool = require("baikaifa-openapi-tool");
const { resolve } = require("path");

const outputDir = resolve(__dirname, "./service");

const readDocUrlAndCreateTsFile = (url) => {
  const openApiTool = new OpenApiTool({ url });
  openApiTool.generateService({
    template: "axios",
    importText: `
import Network from "../network";
const axios = Network;
    `,
    typescript: true,
    outputDir,
  });

}

function main() {
  let url = process.argv[2]
  if (!url) {
    console.log("请输入文档url")
    return
  }
  readDocUrlAndCreateTsFile(url)
}

// 判断模块是否直接被运行（不是被require导入）
if (require.main === module) {
  main();
} else {
  module.exports = readDocUrlAndCreateTsFile;
}

