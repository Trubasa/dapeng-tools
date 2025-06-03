# 代码文档: koc-share-dialog

*本文档由c2m工具自动生成于 D:\project_workplace\xy2-miniapp-assistance\src\minapp-code\app-components\koc-share-dialog*

## 目录

- [koc-share-dialog.js](#koc-share-dialogjs)
- [koc-share-dialog.json](#koc-share-dialogjson)


### koc-share-dialog.js
```javascript
const { default: images } = require("../../config/scanImages");
import { saveImageOrShowShareMenu, sleep } from "../../utils/commonUtil";
const { EVENT_ENUM, VIEW_ENUM, BTN_ENUM } = require("../../enum/enum");
const { default: bus } = require("../../utils/bus");
import { logicUtils } from "@/logic/logicUtils";
import { allLogic } from "../../logic/allLogic";
import { store } from "@/utils/store";
import * as common from "@/utils/commonUtil";
import {
  hideLoading,
  loading,
  saveImage,
  saveImageWidthAuthorize,
  showLoading,
  toast,
} from "../../utils/commonUtil";
import { udataClick } from "../../utils/record";
const myKocLogicHook = logicUtils.useLogicHook("myKocLogic");
const newServerLogicHook = logicUtils.useLogicHook("newServerLogic");
const shareLogicHook = logicUtils.useLogicHook("shareLogic");

// components/reward-dialog/reward-dialog.ts
Component({
  options: {
    multipleSlots: true,
  },
  /**
   * 组件的属性列表
   */
  properties: {
    title: {
      type: String,
      default: "",
    },
  },

  /**
   * 组件的初始数据
   */
  data: {
    //#region [logic]
    myKocLogic: allLogic.myKocLogic,
    newServerLogic: allLogic.newServerLogic,
    shareLogic: allLogic.shareLogic,
    //#endregion
    isShow: store.isKocDialogOpen,
    painterWechatGroup: {
      width: "220px",
      height: "220px",
      background: "#fff",
      views: [
        {
          type: "qrcode",
          content: "https://www.baidu.com",
          css: {
            left: "10px",
            top: "10px",
            width: "200px",
            height: "200px",
          },
        },
      ],
    },
    painterAppointment: {
      width: "220px",
      height: "220px",
      background: "#fff",
      views: [
        {
          type: "qrcode",
          content: "https://www.google.com",
          css: {
            left: "10px",
            top: "10px",
            width: "200px",
            height: "200px",
          },
        },
      ],
    },
    shareCoverPainterData: null,
    qrcodeWechatGroup: null,
    qrcodeAppoinment: null,
    isInitShareCover: false,
  },

  /**
   * 组件的方法列表
   */
  methods: {
    //#region [logic] painter 成功和失败回调
    appointmentQrcodeReady(res) {
      this.setData({
        qrcodeAppoinment: res.detail.path,
      });
    },
    appointmentQrcodeError(err) {
      //todo
    },
    wechatGroupQrcodeReady(res) {
      this.setData({
        qrcodeWechatGroup: res.detail.path,
      });
    },
    wechatGroupQrcodeError(err) {
      //todo
    },
    async shareCoverReady(res) {
      saveImageOrShowShareMenu(res.detail.path);
      hideLoading();
    },
    shareCoverError(err) {
      // todo
      hideLoading();
    },
    saveShareCover() {
      udataClick(VIEW_ENUM.APPOINTMENT, BTN_ENUM.KOC_COVER_SAVE);
      this.setData({
        isInitShareCover: false,
      });
      showLoading();
      this.setData({
        shareCoverPainterData: allLogic.myKocLogic.getPainterData(),
        isInitShareCover: true,
      });
    },
    toShare() {
      udataClick(VIEW_ENUM.APPOINTMENT, BTN_ENUM.KOC_SAHRE_BTN);
    },
    // #endregion
    show(options = {}) {
      store.isKocDialogOpen = true;
      this.setData({
        isShow: store.isKocDialogOpen,
      });
    },
    hide() {
      store.isKocDialogOpen = false;
      this.setData({
        isShow: store.isKocDialogOpen,
      });
    },
    copyCode() {
      allLogic.myKocLogic.copyCode();
    },
  },
  lifetimes: {
    attached: function () {
      //#region [logic] init
      myKocLogicHook.bindThis(this);
      myKocLogicHook.registerEvents();

      newServerLogicHook.bindThis(this);
      newServerLogicHook.registerEvents();

      shareLogicHook.bindThis(this);
      shareLogicHook.registerEvents();
      //#endregion

      this.showHandler = this.show.bind(this);
      bus.$on(EVENT_ENUM.SHOW_KOC_SHARE_DIALOG, this.showHandler);
    },
    detached: function () {
      //#region [logic] destroy
      myKocLogicHook.unRegisterEvents();
      newServerLogicHook.unRegisterEvents();
      shareLogicHook.unRegisterEvents();
      //#endregion

      bus.$off(EVENT_ENUM.SHOW_KOC_SHARE_DIALOG, this.showHandler);
    },
  },
});

```

### koc-share-dialog.json
```json
{
  "component": true,
  "styleIsolation": "apply-shared",
  "usingComponents": {
    "painter": "/lib/painter/painter"
  }
}

```

