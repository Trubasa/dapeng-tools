const fs = require('fs');
const path = require('path');

function printTree(dir, prefix = '') {
    // 只有在首次调用时（即没有前缀时）打印目录名称
    if (prefix === '') {
        console.log(dir);  // 打印当前目录路径
    }

    const files = fs.readdirSync(dir);

    files.forEach((file, index) => {
        const filePath = path.join(dir, file);
        const isLast = index === files.length - 1;
        const stats = fs.statSync(filePath);

        if (stats.isDirectory()) {
            console.log(`${prefix}${isLast ? '└─' : '├─'} ${file}`);
            printTree(filePath, `${prefix}${isLast ? '  ' : '| '}`);
        } else {
            console.log(`${prefix}${isLast ? '└─' : '├─'} ${file}`);
        }
    });
}

function main() {
    let dir = process.argv[2] || process.cwd();  // 接收命令行参数或默认使用当前工作目录
    printTree(dir);
}

// 判断模块是否直接被运行（不是被require导入）
if (require.main === module) {
    main();
} else {
    module.exports = printTree;
}