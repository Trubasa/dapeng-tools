const OpenApiTool = require("baikaifa-openapi-tool");
const { resolve, join } = require("path");
const fs = require("fs").promises; // 使用 promise 版本的 fs 模块

const outputDir = resolve(__dirname, "./service");

const readDocUrlAndCreateTsFile = async (url) => {
  const templatePath = join(__dirname, 'templates', 'axiosTemplate.cjs');
  try {
    const importText = await fs.readFile(templatePath, 'utf8'); // 异步读取模板文件

    const openApiTool = new OpenApiTool({ url });
    openApiTool.generateService({
      template: "axios",
      importText, // 使用读取到的模板内容
      typescript: true,
      outputDir,
    });
  } catch (error) {
    console.error('Error reading the axios template:', error);
  }
}

async function main() {
  let url = process.argv[2];
  if (!url) {
    console.log("请输入文档url");
    return;
  }
  await readDocUrlAndCreateTsFile(url); // 这里需要等待异步操作完成
}

// 判断模块是否直接被运行（不是被require导入）
if (require.main === module) {
  main();
} else {
  module.exports = readDocUrlAndCreateTsFile;
}