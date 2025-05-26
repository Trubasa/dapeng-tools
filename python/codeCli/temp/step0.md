# 代码文档: test-workplace

*本文档由c2m工具自动生成于 G:\test\test-workplace*

## 目录

- [.vite\deps_temp_be5e8324\package.json](#vite\deps_temp_be5e8324\packagejson)
- [index.html](#indexhtml)
- [package.json](#packagejson)
- [src\App.css](#src\Appcss)
- [src\App.tsx](#src\Apptsx)
- [src\components\ContextMenu.css](#src\components\ContextMenucss)
- [src\components\ContextMenu.tsx](#src\components\ContextMenutsx)
- [src\components\CustomNodes\InputNode.tsx](#src\components\CustomNodes\InputNodetsx)
- [src\components\CustomNodes\OutputNode.tsx](#src\components\CustomNodes\OutputNodetsx)
- [src\components\CustomNodes\ProcessNode.tsx](#src\components\CustomNodes\ProcessNodetsx)
- [src\index.css](#src\indexcss)
- [src\main.tsx](#src\maintsx)
- [src\vite-env.d.ts](#src\vite-envdts)
- [tsconfig.json](#tsconfigjson)
- [tsconfig.node.json](#tsconfignodejson)
- [vite.config.ts](#viteconfigts)


### .vite\deps_temp_be5e8324\package.json
```json
{
  "type": "module"
}

```

### index.html
```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/svg+xml" href="/vite.svg" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>React Flow Workflow Builder</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.tsx"></script>
  </body>
</html>

```

### package.json
```json
{
  "name": "react-flow-workflow-builder",
  "private": true,
  "version": "0.0.1",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "tsc && vite build",
    "lint": "eslint . --ext ts,tsx --report-unused-disable-directives --max-warnings 0",
    "preview": "vite preview"
  },
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "@xyflow/react": "^11.11.3"
  },
  "devDependencies": {
    "@types/react": "^18.2.66",
    "@types/react-dom": "^18.2.22",
    "@typescript-eslint/eslint-plugin": "^7.2.0",
    "@typescript-eslint/parser": "^7.2.0",
    "@vitejs/plugin-react": "^4.2.1",
    "eslint": "^8.57.0",
    "eslint-plugin-react-hooks": "^4.6.0",
    "eslint-plugin-react-refresh": "^0.4.6",
    "typescript": "^5.2.2",
    "vite": "^5.2.0"
  }
}

```

### src\App.css
```css

/* App.tsx specific styles */
.app-container {
  display: flex;
  flex-direction: row;
  width: 100%;
  height: 100%;
  background-color: #1a192b; /* 深色背景 */
}

.sidebar {
  width: 200px;
  padding: 15px;
  border-right: 1px solid #444;
  background-color: #2c2c3e; /* 侧边栏背景 */
  color: #f0f0f0; /* 浅色文字 */
  display: flex;
  flex-direction: column;
  gap: 10px;
  overflow-y: auto; /* 新增：如果侧边栏内容过多，允许滚动 */
}

.sidebar .description {
  margin-bottom: 10px;
  font-size: 0.9em;
  color: #aaa;
}

.sidebar-node {
  padding: 10px;
  border: 1px solid #555;
  border-radius: 4px;
  cursor: grab;
  text-align: center;
  background-color: #3a3a52; /* 节点选项背景 */
  transition: background-color 0.2s ease;
}

.sidebar-node:hover {
  background-color: #4a4a62; /* 节点选项悬停背景 */
}

.input-node-palette {
  border-left: 5px solid #76d7c4; /* 绿色主题色 */
}
.process-node-palette {
  border-left: 5px solid #f7dc6f; /* 黄色主题色 */
}
.output-node-palette {
  border-left: 5px solid #ec7063; /* 红色主题色 */
}


.reactflow-wrapper {
  flex-grow: 1;
  height: 100%;
  position: relative; /* 新增：确保 context menu 相对于此容器定位（如果需要） */
}

/* Custom Node Styles (can also be in their respective component files) */
.custom-node {
  padding: 10px 15px;
  border-radius: 5px;
  border: 1px solid #333;
  font-size: 12px;
  color: #fff;
  min-width: 150px;
  text-align: center;
}

.input-node {
  background: #2c3e50; /* 深蓝灰色 */
  border-color: #76d7c4; /* 绿色边框 */
  border-width: 2px;
}

.process-node {
  background: #8e44ad; /* 紫色 */
  border-color: #f7dc6f; /* 黄色边框 */
  border-width: 2px;
}

.output-node {
  background: #c0392b; /* 深红色 */
  border-color: #ec7063; /* 浅红色边框 */
  border-width: 2px;
}

.custom-node .react-flow__handle {
  width: 8px;
  height: 8px;
  background: #555;
  border-radius: 50%;
}

.custom-node .react-flow__handle-top {
  top: -5px;
}
.custom-node .react-flow__handle-bottom {
  bottom: -5px;
}
.custom-node .react-flow__handle-left {
  left: -5px;
}
.custom-node .react-flow__handle-right {
  right: -5px;
}

/* Styles for new sidebar buttons */
.sidebar-button {
  padding: 8px 10px;
  border: 1px solid #555;
  border-radius: 4px;
  cursor: pointer;
  text-align: center;
  background-color: #3a3a52; /* Use similar bg as draggable nodes */
  color: #f0f0f0; /* Light text */
  transition: background-color 0.2s ease;
  margin-top: 5px; /* Add some spacing between buttons */
  font-size: 0.9em;
}

.sidebar-button:hover {
  background-color: #4a4a62; /* Darken on hover */
}

/* 新增：确保 React Flow 控件在 ContextMenu 之上 (如果需要调整 z-index) */
/* .react-flow__controls {
  z-index: 5; 
} */

```

### src\App.tsx
```tsx

import React, { useState, useCallback, useRef, DragEvent, MouseEvent, useEffect } from 'react';
import {
  ReactFlow,
  ReactFlowProvider,
  addEdge,
  useNodesState,
  useEdgesState,
  Controls,
  Background,
  MiniMap,
  Node,
  Edge,
  Connection,
  XYPosition,
  NodeTypes,
  ReactFlowInstance,
  OnNodesChange,
  OnEdgesChange,
} from '@xyflow/react';

import InputNode from './components/CustomNodes/InputNode';
import ProcessNode from './components/CustomNodes/ProcessNode';
import OutputNode from './components/CustomNodes/OutputNode';
import ContextMenu, { ContextMenuItem } from './components/ContextMenu'; // 新增：导入 ContextMenu

import './App.css';

// localStorage keys
const LOCALSTORAGE_KEY_NODES = 'reactflow_nodes';
const LOCALSTORAGE_KEY_EDGES = 'reactflow_edges';
const LOCALSTORAGE_KEY_ID_COUNTER = 'reactflow_id_counter';

// 初始节点数据 (hardcoded, will be overridden by localStorage if available)
const initialNodesData: Node[] = [
  {
    id: 'node_1', // 修改：统一ID格式
    type: 'inputNode',
    data: { label: 'Start Workflow' },
    position: { x: 250, y: 5 },
  },
  {
    id: 'node_2', // 修改：统一ID格式
    type: 'processNode',
    data: { label: 'Process Data' },
    position: { x: 250, y: 150 },
  },
  {
    id: 'node_3', // 修改：统一ID格式
    type: 'outputNode',
    data: { label: 'End Workflow' },
    position: { x: 250, y: 300 },
  },
];

// 初始边数据 (hardcoded, will be overridden by localStorage if available)
const initialEdgesData: Edge[] = [
  { id: 'e_node_1-node_2', source: 'node_1', target: 'node_2', animated: true }, // 修改：对应ID格式
  { id: 'e_node_2-node_3', source: 'node_2', target: 'node_3', animated: true }, // 修改：对应ID格式
];

const nodeTypes: NodeTypes = {
  inputNode: InputNode,
  processNode: ProcessNode,
  outputNode: OutputNode,
};

interface ContextMenuState {
  id?: string; // For node context menu, this will be node ID
  top: number;
  left: number;
  items: ContextMenuItem[];
  flowPosition?: XYPosition; // For pane context menu
}

function App() {
  const reactFlowWrapper = useRef<HTMLDivElement>(null);
  const idCounter = useRef<number>(4); // 用于生成新节点ID的计数器

  const [nodes, setNodes, onNodesChangeInternal] = useNodesState([]);
  const [edges, setEdges, onEdgesChangeInternal] = useEdgesState([]);
  const [reactFlowInstance, setReactFlowInstance] = useState<ReactFlowInstance | null>(null);
  const [contextMenu, setContextMenu] = useState<ContextMenuState | null>(null);

  // 初始化ID计数器
  const initializeIdCounter = (loadedNodes?: Node[]) => {
    const savedCounter = localStorage.getItem(LOCALSTORAGE_KEY_ID_COUNTER);
    if (savedCounter) {
      idCounter.current = parseInt(savedCounter, 10);
      return;
    }

    let maxIdNum = 0;
    const nodesToScan = loadedNodes || initialNodesData;
    if (nodesToScan.length > 0) {
        nodesToScan.forEach(node => {
        if (node.id.startsWith('node_')) {
          const num = parseInt(node.id.split('_')[1], 10);
          if (!isNaN(num) && num > maxIdNum) {
            maxIdNum = num;
          }
        }
      });
      idCounter.current = maxIdNum + 1;
    } else {
      idCounter.current = 1; // Start from 1 if no nodes
    }
  };
  
  const getId = useCallback(() => {
    const newId = `node_${idCounter.current++}`;
    localStorage.setItem(LOCALSTORAGE_KEY_ID_COUNTER, idCounter.current.toString()); // 保存计数器状态
    return newId;
  }, []);


  // 加载流程
  const loadFlow = useCallback(() => {
    const storedNodes = localStorage.getItem(LOCALSTORAGE_KEY_NODES);
    const storedEdges = localStorage.getItem(LOCALSTORAGE_KEY_EDGES);

    const nodesToLoad = storedNodes ? JSON.parse(storedNodes) : initialNodesData;
    const edgesToLoad = storedEdges ? JSON.parse(storedEdges) : initialEdgesData;
    
    initializeIdCounter(nodesToLoad); // 初始化或更新ID计数器

    setNodes(nodesToLoad);
    setEdges(edgesToLoad);

    if (reactFlowInstance) {
      // Ensure a slight delay for nodes to render before fitting view
      setTimeout(() => reactFlowInstance.fitView(), 0);
    }
    console.log('Flow loaded from localStorage.');
  }, [setNodes, setEdges, reactFlowInstance, initializeIdCounter]); // initializeIdCounter is stable

  // 保存流程
  const saveFlow = useCallback(() => {
    if (nodes.length > 0) { // Only save if there are nodes
        localStorage.setItem(LOCALSTORAGE_KEY_NODES, JSON.stringify(nodes));
        localStorage.setItem(LOCALSTORAGE_KEY_EDGES, JSON.stringify(edges));
        localStorage.setItem(LOCALSTORAGE_KEY_ID_COUNTER, idCounter.current.toString());
        console.log('Flow saved to localStorage.');
        alert('Workflow saved!');
    } else {
        // Clear localStorage if there are no nodes to save (optional)
        localStorage.removeItem(LOCALSTORAGE_KEY_NODES);
        localStorage.removeItem(LOCALSTORAGE_KEY_EDGES);
        localStorage.removeItem(LOCALSTORAGE_KEY_ID_COUNTER);
        console.log('Flow cleared from localStorage as it is empty.');
        alert('Workflow is empty, cleared saved data.');
    }
  }, [nodes, edges, idCounter]);

  // 初始加载
  useEffect(() => {
    loadFlow();
  }, [loadFlow]); // loadFlow is memoized

  // 自动保存 (当节点或边变化时)
  useEffect(() => {
    if (nodes.length > 0 || edges.length > 0) { // Avoid saving empty initial state before load
        localStorage.setItem(LOCALSTORAGE_KEY_NODES, JSON.stringify(nodes));
    }
  }, [nodes]);

  useEffect(() => {
    if (nodes.length > 0 || edges.length > 0) { // Avoid saving empty initial state before load
        localStorage.setItem(LOCALSTORAGE_KEY_EDGES, JSON.stringify(edges));
    }
  }, [edges]);


  // 包装 onNodesChange 和 onEdgesChange 以清除 contextMenu
  const onNodesChange: OnNodesChange = (changes) => {
    onNodesChangeInternal(changes);
    setContextMenu(null); // 关闭菜单当节点变化时
  };

  const onEdgesChange: OnEdgesChange = (changes) => {
    onEdgesChangeInternal(changes);
    setContextMenu(null); // 关闭菜单当边变化时
  };
  
  const onConnect = useCallback(
    (params: Connection | Edge) => {
      setEdges((eds) => addEdge(params, eds));
      setContextMenu(null);
    },
    [setEdges]
  );

  const onDragOver = useCallback((event: DragEvent) => {
    event.preventDefault();
    event.dataTransfer.dropEffect = 'move';
  }, []);

  const onDrop = useCallback(
    (event: DragEvent) => {
      event.preventDefault();
      setContextMenu(null);

      if (!reactFlowWrapper.current || !reactFlowInstance) {
        return;
      }
      
      const type = event.dataTransfer.getData('application/reactflow');
      if (typeof type === 'undefined' || !type) {
        return;
      }

      const reactFlowBounds = reactFlowWrapper.current.getBoundingClientRect();
      const position = reactFlowInstance.screenToFlowPosition({
        x: event.clientX - reactFlowBounds.left,
        y: event.clientY - reactFlowBounds.top,
      });
      
      const newNode: Node = {
        id: getId(),
        type,
        position,
        data: { label: `${type.replace('Node','')} Node` },
      };

      setNodes((nds) => nds.concat(newNode));
    },
    [reactFlowInstance, setNodes, getId]
  );
  
  const onDragStart = (event: DragEvent, nodeType: string) => {
    event.dataTransfer.setData('application/reactflow', nodeType);
    event.dataTransfer.effectAllowed = 'move';
  };

  const onEdgeContextMenu = useCallback(
    (event: MouseEvent, edge: Edge) => {
      event.preventDefault();
      setContextMenu(null); // 关闭其他可能打开的菜单
      if (window.confirm('Are you sure you want to delete this connection?')) {
        setEdges((eds) => eds.filter((e) => e.id !== edge.id));
      }
    },
    [setEdges]
  );

  // 新增：处理画布右键菜单
  const onPaneContextMenu = useCallback(
    (event: MouseEvent) => {
      event.preventDefault();
      if (!reactFlowInstance || !reactFlowWrapper.current) return;

      const reactFlowBounds = reactFlowWrapper.current.getBoundingClientRect();
      const flowPosition = reactFlowInstance.screenToFlowPosition({
        x: event.clientX - reactFlowBounds.left,
        y: event.clientY - reactFlowBounds.top,
      });

      setContextMenu({
        id: undefined,
        top: event.clientY,
        left: event.clientX,
        flowPosition: flowPosition,
        items: [
          { label: 'Create Input Node', action: () => addNode('inputNode', flowPosition) },
          { label: 'Create Process Node', action: () => addNode('processNode', flowPosition) },
          { label: 'Create Output Node', action: () => addNode('outputNode', flowPosition) },
        ],
      });
    },
    [reactFlowInstance, getId, setNodes] // addNode will be defined below
  );

  // 新增：处理节点右键菜单
  const onNodeContextMenu = useCallback(
    (event: MouseEvent, node: Node) => {
      event.preventDefault();
      setContextMenu({
        id: node.id,
        top: event.clientY,
        left: event.clientX,
        items: [
          { label: 'Delete Node', action: () => deleteNode(node.id) },
          // Future actions for nodes can be added here
        ],
      });
    },
    [setNodes, setEdges] // deleteNode will be defined below
  );
  
  // 新增：添加节点函数
  const addNode = useCallback((type: string, position: XYPosition) => {
    const newNode: Node = {
      id: getId(),
      type,
      position,
      data: { label: `${type.replace('Node','')} Node` },
    };
    setNodes((nds) => nds.concat(newNode));
    setContextMenu(null); // Close context menu
  }, [getId, setNodes]);

  // 新增：删除节点函数
  const deleteNode = useCallback((nodeId: string) => {
    setNodes((nds) => nds.filter((n) => n.id !== nodeId));
    setEdges((eds) => eds.filter((e) => e.source !== nodeId && e.target !== nodeId));
    setContextMenu(null); // Close context menu
  }, [setNodes, setEdges]);

  // 新增：点击画布关闭菜单
  const onPaneClick = useCallback(() => {
    setContextMenu(null);
  }, []);


  return (
    <div className="app-container">
      <ReactFlowProvider>
        <div className="sidebar">
          <div className="description">Drag nodes to the canvas:</div>
          <div 
            className="sidebar-node input-node-palette" 
            onDragStart={(event) => onDragStart(event, 'inputNode')} 
            draggable
          >
            Start Node
          </div>
          <div 
            className="sidebar-node process-node-palette" 
            onDragStart={(event) => onDragStart(event, 'processNode')} 
            draggable
          >
            Process Node
          </div>
          <div 
            className="sidebar-node output-node-palette" 
            onDragStart={(event) => onDragStart(event, 'outputNode')} 
            draggable
          >
            End Node
          </div>
          <div className="description" style={{marginTop: '20px'}}>Manage Workflow:</div>
          <button className="sidebar-button" onClick={saveFlow}>Save Flow</button>
          <button className="sidebar-button" onClick={loadFlow}>Load Flow</button>
        </div>
        <div className="reactflow-wrapper" ref={reactFlowWrapper}>
          <ReactFlow
            nodes={nodes}
            edges={edges}
            onNodesChange={onNodesChange}
            onEdgesChange={onEdgesChange}
            onConnect={onConnect}
            nodeTypes={nodeTypes}
            onInit={setReactFlowInstance}
            onDrop={onDrop}
            onDragOver={onDragOver}
            onEdgeContextMenu={onEdgeContextMenu}
            onPaneContextMenu={onPaneContextMenu} // 新增
            onNodeContextMenu={onNodeContextMenu} // 新增
            onPaneClick={onPaneClick} // 新增：点击画布关闭菜单
            fitView
            attributionPosition="bottom-left"
          >
            <Controls />
            <MiniMap />
            <Background gap={12} size={1} />
          </ReactFlow>
          {contextMenu && ( // 新增：渲染上下文菜单
            <ContextMenu
              x={contextMenu.left}
              y={contextMenu.top}
              items={contextMenu.items}
              onClose={() => setContextMenu(null)}
            />
          )}
        </div>
      </ReactFlowProvider>
    </div>
  );
}

export default App;

```

### src\components\ContextMenu.css
```css

.context-menu {
  position: fixed; /* 使用 fixed 定位，相对于视口 */
  background-color: #3e3e5a; /* 深色背景，比侧边栏稍亮 */
  border: 1px solid #555;
  border-radius: 5px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3); /* 更明显的阴影 */
  z-index: 10000; /* 确保在最上层 */
  padding: 6px 0;
  color: #e0e0e0; /* 浅色文字 */
  min-width: 180px; /* 最小宽度 */
  font-size: 14px;
}

.context-menu ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.context-menu li {
  padding: 10px 18px; /* 增加内边距 */
  cursor: pointer;
  transition: background-color 0.15s ease-in-out;
}

.context-menu li:hover {
  background-color: #4f4f70; /* 悬停时更亮的背景 */
}

.context-menu li.disabled {
  color: #888;
  cursor: not-allowed;
  background-color: transparent; /* 禁用项无悬停效果 */
}

.context-menu li.disabled:hover {
  background-color: transparent;
}

```

### src\components\ContextMenu.tsx
```tsx

import React from 'react';
import './ContextMenu.css'; // 引入上下文菜单样式

export interface ContextMenuItem {
  label: string;
  action: () => void;
  disabled?: boolean; // 可选：禁用菜单项
}

interface ContextMenuProps {
  x: number;
  y: number;
  items: ContextMenuItem[];
  onClose: () => void;
}

const ContextMenu: React.FC<ContextMenuProps> = ({ x, y, items, onClose }) => {
  const handleItemClick = (itemAction: () => void) => {
    itemAction();
    onClose(); // 执行动作后关闭菜单
  };

  // 防止菜单内部点击触发外部的 onPaneClick (如果它存在并关闭菜单)
  const handleMenuClick = (event: React.MouseEvent) => {
    event.stopPropagation();
  };

  return (
    <div
      className="context-menu"
      style={{ top: y, left: x }}
      onClick={handleMenuClick} // 阻止事件冒泡
      onContextMenu={(e) => e.preventDefault()} // 防止在菜单上再次触发浏览器默认右键菜单
    >
      <ul>
        {items.map((item, index) => (
          <li
            key={index}
            onClick={() => !item.disabled && handleItemClick(item.action)}
            className={item.disabled ? 'disabled' : ''}
          >
            {item.label}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ContextMenu;

```

### src\components\CustomNodes\InputNode.tsx
```tsx
import React, { memo } from 'react';
import { Handle, Position, NodeProps } from '@xyflow/react';

// memoized لتجنب إعادة العرض غير الضرورية
const InputNode: React.FC<NodeProps<{ label: string }>> = ({ data, isConnectable }) => {
  return (
    <div className="custom-node input-node">
      <Handle
        type="source"
        position={Position.Bottom}
        isConnectable={isConnectable}
      />
      <div>{data.label || 'Input Node'}</div>
    </div>
  );
};

export default memo(InputNode);

```

### src\components\CustomNodes\OutputNode.tsx
```tsx
import React, { memo } from 'react';
import { Handle, Position, NodeProps } from '@xyflow/react';

const OutputNode: React.FC<NodeProps<{ label: string }>> = ({ data, isConnectable }) => {
  return (
    <div className="custom-node output-node">
      <Handle
        type="target"
        position={Position.Top}
        isConnectable={isConnectable}
      />
      <div>{data.label || 'Output Node'}</div>
    </div>
  );
};

export default memo(OutputNode);

```

### src\components\CustomNodes\ProcessNode.tsx
```tsx
import React, { memo } from 'react';
import { Handle, Position, NodeProps } from '@xyflow/react';

const ProcessNode: React.FC<NodeProps<{ label: string }>> = ({ data, isConnectable }) => {
  return (
    <div className="custom-node process-node">
      <Handle
        type="target"
        position={Position.Top}
        isConnectable={isConnectable}
      />
      <div>{data.label || 'Process Node'}</div>
      <Handle
        type="source"
        position={Position.Bottom}
        isConnectable={isConnectable}
      />
      {/* 可以添加左右 Handle */}
      {/* <Handle type="source" position={Position.Right} id="a" isConnectable={isConnectable} /> */}
      {/* <Handle type="target" position={Position.Left} id="b" isConnectable={isConnectable} /> */}
    </div>
  );
};

export default memo(ProcessNode);

```

### src\index.css
```css
/* 全局基础样式 */
:root {
  font-family: Inter, system-ui, Avenir, Helvetica, Arial, sans-serif;
  line-height: 1.5;
  font-weight: 400;

  color-scheme: light dark;
  color: rgba(255, 255, 255, 0.87);
  background-color: #242424;

  font-synthesis: none;
  text-rendering: optimizeLegibility;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

body {
  margin: 0;
  display: flex;
  place-items: center;
  min-width: 320px;
  min-height: 100vh;
}

#root {
  width: 100vw;
  height: 100vh;
  margin: 0 auto;
  text-align: center;
  display: flex; /* Ensure App takes full height/width */
}

/* React Flow 默认主题样式 (如果不想用 theme-default.css, 可以自定义) */
/* .react-flow__minimap {
  background-color: #333;
}
.react-flow__controls button {
  background-color: #444;
  border-color: #555;
}
.react-flow__controls button:hover {
  background-color: #555;
}
.react-flow__edge-path {
  stroke: #b1b1b7;
} */

```

### src\main.tsx
```tsx
import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.tsx'
import './index.css'
import '@xyflow/react/dist/style.css'; // React Flow 基础样式
// import '@xyflow/react/dist/theme-default.css'; // 可选：React Flow 默认主题

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)

```

### src\vite-env.d.ts
```typescript
/// <reference types="vite/client" />

```

### tsconfig.json
```json
{
  "compilerOptions": {
    "target": "ES2020",
    "useDefineForClassFields": true,
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "skipLibCheck": true,

    /* Bundler mode */
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "react-jsx",

    /* Linting */
    "strict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noFallthroughCasesInSwitch": true,

    /* Path Aliases */
    "baseUrl": ".",
    "paths": {
      "@/*": ["src/*"]
    }
  },
  "include": ["src"],
  "references": [{ "path": "./tsconfig.node.json" }]
}

```

### tsconfig.node.json
```json
{
  "compilerOptions": {
    "composite": true,
    "skipLibCheck": true,
    "module": "ESNext",
    "moduleResolution": "bundler",
    "allowSyntheticDefaultImports": true,
    "strict": true
  },
  "include": ["vite.config.ts"]
}

```

### vite.config.ts
```typescript
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
})

```

