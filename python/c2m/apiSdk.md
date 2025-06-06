# 代码文档: lsdmxmp-client

*本文档由c2m工具自动生成于 G:\code\lsdmxmp-client*

## 目录

- [node_modules\.package-lock.json](#node_modules\package-lockjson)
- [node_modules\@everdev\lsdmxmp-client\api.ts](#node_modules\@everdev\lsdmxmp-client\apits)
- [node_modules\@everdev\lsdmxmp-client\base.ts](#node_modules\@everdev\lsdmxmp-client\basets)
- [node_modules\@everdev\lsdmxmp-client\common.ts](#node_modules\@everdev\lsdmxmp-client\commonts)
- [node_modules\@everdev\lsdmxmp-client\configuration.ts](#node_modules\@everdev\lsdmxmp-client\configurationts)
- [node_modules\@everdev\lsdmxmp-client\git_push.sh](#node_modules\@everdev\lsdmxmp-client\git_pushsh)
- [node_modules\@everdev\lsdmxmp-client\index.ts](#node_modules\@everdev\lsdmxmp-client\indexts)
- [node_modules\@everdev\lsdmxmp-client\package.json](#node_modules\@everdev\lsdmxmp-client\packagejson)
- [node_modules\@everdev\lsdmxmp-client\tsconfig.json](#node_modules\@everdev\lsdmxmp-client\tsconfigjson)
- [node_modules\axios\CHANGELOG.md](#node_modules\axios\CHANGELOGmd)
- [node_modules\axios\README.md](#node_modules\axios\READMEmd)
- [node_modules\axios\SECURITY.md](#node_modules\axios\SECURITYmd)
- [node_modules\axios\UPGRADE_GUIDE.md](#node_modules\axios\UPGRADE_GUIDEmd)
- [node_modules\axios\index.d.ts](#node_modules\axios\indexdts)
- [node_modules\axios\index.js](#node_modules\axios\indexjs)
- [node_modules\axios\lib\adapters\README.md](#node_modules\axios\lib\adapters\READMEmd)
- [node_modules\axios\lib\adapters\http.js](#node_modules\axios\lib\adapters\httpjs)
- [node_modules\axios\lib\adapters\xhr.js](#node_modules\axios\lib\adapters\xhrjs)
- [node_modules\axios\lib\axios.js](#node_modules\axios\lib\axiosjs)
- [node_modules\axios\lib\cancel\Cancel.js](#node_modules\axios\lib\cancel\Canceljs)
- [node_modules\axios\lib\cancel\CancelToken.js](#node_modules\axios\lib\cancel\CancelTokenjs)
- [node_modules\axios\lib\cancel\isCancel.js](#node_modules\axios\lib\cancel\isCanceljs)
- [node_modules\axios\lib\core\Axios.js](#node_modules\axios\lib\core\Axiosjs)
- [node_modules\axios\lib\core\InterceptorManager.js](#node_modules\axios\lib\core\InterceptorManagerjs)
- [node_modules\axios\lib\core\README.md](#node_modules\axios\lib\core\READMEmd)
- [node_modules\axios\lib\core\buildFullPath.js](#node_modules\axios\lib\core\buildFullPathjs)
- [node_modules\axios\lib\core\createError.js](#node_modules\axios\lib\core\createErrorjs)
- [node_modules\axios\lib\core\dispatchRequest.js](#node_modules\axios\lib\core\dispatchRequestjs)
- [node_modules\axios\lib\core\enhanceError.js](#node_modules\axios\lib\core\enhanceErrorjs)
- [node_modules\axios\lib\core\mergeConfig.js](#node_modules\axios\lib\core\mergeConfigjs)
- [node_modules\axios\lib\core\settle.js](#node_modules\axios\lib\core\settlejs)
- [node_modules\axios\lib\core\transformData.js](#node_modules\axios\lib\core\transformDatajs)
- [node_modules\axios\lib\defaults.js](#node_modules\axios\lib\defaultsjs)
- [node_modules\axios\lib\helpers\README.md](#node_modules\axios\lib\helpers\READMEmd)
- [node_modules\axios\lib\helpers\bind.js](#node_modules\axios\lib\helpers\bindjs)
- [node_modules\axios\lib\helpers\buildURL.js](#node_modules\axios\lib\helpers\buildURLjs)
- [node_modules\axios\lib\helpers\combineURLs.js](#node_modules\axios\lib\helpers\combineURLsjs)
- [node_modules\axios\lib\helpers\cookies.js](#node_modules\axios\lib\helpers\cookiesjs)
- [node_modules\axios\lib\helpers\deprecatedMethod.js](#node_modules\axios\lib\helpers\deprecatedMethodjs)
- [node_modules\axios\lib\helpers\isAbsoluteURL.js](#node_modules\axios\lib\helpers\isAbsoluteURLjs)
- [node_modules\axios\lib\helpers\isAxiosError.js](#node_modules\axios\lib\helpers\isAxiosErrorjs)
- [node_modules\axios\lib\helpers\isURLSameOrigin.js](#node_modules\axios\lib\helpers\isURLSameOriginjs)
- [node_modules\axios\lib\helpers\normalizeHeaderName.js](#node_modules\axios\lib\helpers\normalizeHeaderNamejs)
- [node_modules\axios\lib\helpers\parseHeaders.js](#node_modules\axios\lib\helpers\parseHeadersjs)
- [node_modules\axios\lib\helpers\spread.js](#node_modules\axios\lib\helpers\spreadjs)
- [node_modules\axios\lib\helpers\validator.js](#node_modules\axios\lib\helpers\validatorjs)
- [node_modules\axios\lib\utils.js](#node_modules\axios\lib\utilsjs)
- [node_modules\axios\package.json](#node_modules\axios\packagejson)
- [node_modules\follow-redirects\README.md](#node_modules\follow-redirects\READMEmd)
- [node_modules\follow-redirects\debug.js](#node_modules\follow-redirects\debugjs)
- [node_modules\follow-redirects\http.js](#node_modules\follow-redirects\httpjs)
- [node_modules\follow-redirects\https.js](#node_modules\follow-redirects\httpsjs)
- [node_modules\follow-redirects\index.js](#node_modules\follow-redirects\indexjs)
- [node_modules\follow-redirects\package.json](#node_modules\follow-redirects\packagejson)
- [package-lock.json](#package-lockjson)
- [package.json](#packagejson)


### node_modules\.package-lock.json
```json
{
  "name": "lsdmxmp-client",
  "lockfileVersion": 3,
  "requires": true,
  "packages": {
    "node_modules/@everdev/lsdmxmp-client": {
      "version": "0.0.1-SNAPSHOT-dev",
      "resolved": "https://repo-everdev.nie.netease.com/repository/npm/@everdev/lsdmxmp-client/-/lsdmxmp-client-0.0.1-SNAPSHOT-dev.tgz",
      "integrity": "sha512-aIfDjE8pSlXrzSDGlGqcxmm/yTmwZZjuZefv0RPdR8N4kqbrnou2lckV2ULxV9614eBUlGeLo6IkB4Ik0rKM4g==",
      "dependencies": {
        "axios": "^0.21.1"
      }
    },
    "node_modules/axios": {
      "version": "0.21.4",
      "resolved": "https://repo-everdev.nie.netease.com/repository/npm/axios/-/axios-0.21.4.tgz",
      "integrity": "sha512-ut5vewkiu8jjGBdqpM44XxjuCjq9LAKeHVmoVfHVzy8eHgxxq8SbAVQNovDA8mVi05kP0Ea/n/UzcSHcTJQfNg==",
      "dependencies": {
        "follow-redirects": "^1.14.0"
      }
    },
    "node_modules/follow-redirects": {
      "version": "1.15.9",
      "resolved": "https://repo-everdev.nie.netease.com/repository/npm/follow-redirects/-/follow-redirects-1.15.9.tgz",
      "integrity": "sha512-gew4GsXizNgdoRyqmyfMHyAmXsZDk6mHkSxZFCzW9gwlbtOW44CDtYavM+y+72qD/Vq2l550kMF52DT8fOLJqQ==",
      "funding": [
        {
          "type": "individual",
          "url": "https://github.com/sponsors/RubenVerborgh"
        }
      ],
      "engines": {
        "node": ">=4.0"
      },
      "peerDependenciesMeta": {
        "debug": {
          "optional": true
        }
      }
    }
  }
}

```

### node_modules\@everdev\lsdmxmp-client\api.ts
```typescript
/* tslint:disable */
/* eslint-disable */
/**
 * lsdmx-mp Server API Document
 * lsdmx-mp 服务端接口文档
 *
 * The version of the OpenAPI document: v0.0.1-SNAPSHOT
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


import type { Configuration } from '@everdev/lsdmxmp-client/configuration';
import type { AxiosPromise, AxiosInstance, RawAxiosRequestConfig } from 'axios';
import globalAxios from 'axios';
// Some imports not used depending on template conditions
// @ts-ignore
import { DUMMY_BASE_URL, assertParamExists, setApiKeyToObject, setBasicAuthToObject, setBearerAuthToObject, setOAuthToObject, setSearchParams, serializeDataIfNeeded, toPathString, createRequestFunction } from '@everdev/lsdmxmp-client/common';
import type { RequestArgs } from '@everdev/lsdmxmp-client/base';
// @ts-ignore
import { BASE_PATH, COLLECTION_FORMATS, BaseAPI, RequiredError, operationServerMap } from '@everdev/lsdmxmp-client/base';

/**
 * 
 * @export
 * @interface ActiveActivity
 */
export interface ActiveActivity {
    /**
     * 
     * @type {string}
     * @memberof ActiveActivity
     */
    'id'?: string;
    /**
     * 
     * @type {string}
     * @memberof ActiveActivity
     */
    'name'?: string;
    /**
     * 
     * @type {string}
     * @memberof ActiveActivity
     */
    'description'?: string;
    /**
     * 
     * @type {string}
     * @memberof ActiveActivity
     */
    'createdAt'?: string;
    /**
     * 
     * @type {LotteryCost}
     * @memberof ActiveActivity
     */
    'cost'?: LotteryCost;
    /**
     * 
     * @type {Array<PublicLotteryItem>}
     * @memberof ActiveActivity
     */
    'items'?: Array<PublicLotteryItem>;
}
/**
 * 活动
 * @export
 * @interface Activity
 */
export interface Activity {
    /**
     * 开始时间
     * @type {string}
     * @memberof Activity
     */
    'startAt'?: string;
    /**
     * 结束时间
     * @type {string}
     * @memberof Activity
     */
    'endAt'?: string;
    /**
     * 活动ID
     * @type {string}
     * @memberof Activity
     */
    'id'?: string;
    /**
     * 活动名称
     * @type {string}
     * @memberof Activity
     */
    'name'?: string;
    /**
     * 活动描述
     * @type {string}
     * @memberof Activity
     */
    'desc'?: string;
    /**
     * 活动图片
     * @type {string}
     * @memberof Activity
     */
    'img'?: string;
    /**
     * 是否为发布状态
     * @type {boolean}
     * @memberof Activity
     */
    'publish'?: boolean;
    /**
     * 活动页跳转类型<br>枚举值说明：<br>INTERNAL: 内部;<br>EXTERNAL: 外部
     * @type {string}
     * @memberof Activity
     */
    'jumpType'?: ActivityJumpTypeEnum;
    /**
     * 活动页面地址
     * @type {string}
     * @memberof Activity
     */
    'page'?: string;
    /**
     * 创建时间
     * @type {string}
     * @memberof Activity
     */
    'createdAt'?: string;
    /**
     * 更新时间
     * @type {string}
     * @memberof Activity
     */
    'updatedAt'?: string;
    /**
     * 
     * @type {ActivityStatisticsVO}
     * @memberof Activity
     */
    'statistics'?: ActivityStatisticsVO;
}

export const ActivityJumpTypeEnum = {
    Internal: 'INTERNAL',
    External: 'EXTERNAL'
} as const;

export type ActivityJumpTypeEnum = typeof ActivityJumpTypeEnum[keyof typeof ActivityJumpTypeEnum];

/**
 * 活动保存请求
 * @export
 * @interface ActivityPublishUpdateRequest
 */
export interface ActivityPublishUpdateRequest {
    /**
     * 是否为发布状态
     * @type {boolean}
     * @memberof ActivityPublishUpdateRequest
     */
    'publish': boolean;
}
/**
 * 活动保存请求
 * @export
 * @interface ActivitySaveRequest
 */
export interface ActivitySaveRequest {
    /**
     * 活动名称
     * @type {string}
     * @memberof ActivitySaveRequest
     */
    'name': string;
    /**
     * 活动描述
     * @type {string}
     * @memberof ActivitySaveRequest
     */
    'desc'?: string;
    /**
     * 活动图片
     * @type {string}
     * @memberof ActivitySaveRequest
     */
    'img'?: string;
    /**
     * 活动页跳转类型<br>枚举值说明：<br>INTERNAL: 内部;<br>EXTERNAL: 外部
     * @type {string}
     * @memberof ActivitySaveRequest
     */
    'jumpType'?: ActivitySaveRequestJumpTypeEnum;
    /**
     * 活动页面地址
     * @type {string}
     * @memberof ActivitySaveRequest
     */
    'page'?: string;
    /**
     * 开始时间
     * @type {string}
     * @memberof ActivitySaveRequest
     */
    'startAt'?: string;
    /**
     * 结束时间
     * @type {string}
     * @memberof ActivitySaveRequest
     */
    'endAt'?: string;
}

export const ActivitySaveRequestJumpTypeEnum = {
    Internal: 'INTERNAL',
    External: 'EXTERNAL'
} as const;

export type ActivitySaveRequestJumpTypeEnum = typeof ActivitySaveRequestJumpTypeEnum[keyof typeof ActivitySaveRequestJumpTypeEnum];

/**
 * 活动统计数据VO
 * @export
 * @interface ActivityStatisticsVO
 */
export interface ActivityStatisticsVO {
    /**
     * 邀请者数量
     * @type {number}
     * @memberof ActivityStatisticsVO
     */
    'inviterCount'?: number;
    /**
     * 助力者数量
     * @type {number}
     * @memberof ActivityStatisticsVO
     */
    'helperCount'?: number;
}
/**
 * 
 * @export
 * @interface Address
 */
export interface Address {
    /**
     * 
     * @type {string}
     * @memberof Address
     */
    'province'?: string;
    /**
     * 
     * @type {string}
     * @memberof Address
     */
    'city'?: string;
    /**
     * 
     * @type {string}
     * @memberof Address
     */
    'district'?: string;
    /**
     * 
     * @type {string}
     * @memberof Address
     */
    'detail'?: string;
    /**
     * 
     * @type {string}
     * @memberof Address
     */
    'receiver'?: string;
    /**
     * 
     * @type {string}
     * @memberof Address
     */
    'phone'?: string;
    /**
     * 
     * @type {string}
     * @memberof Address
     */
    'zipCode'?: string;
}
/**
 * 
 * @export
 * @interface AdminEntity
 */
export interface AdminEntity {
    /**
     * 
     * @type {string}
     * @memberof AdminEntity
     */
    'id'?: string;
    /**
     * 
     * @type {string}
     * @memberof AdminEntity
     */
    'createdAt'?: string;
    /**
     * 
     * @type {string}
     * @memberof AdminEntity
     */
    'updatedAt'?: string;
    /**
     * 
     * @type {string}
     * @memberof AdminEntity
     */
    'user'?: string;
}
/**
 * 
 * @export
 * @interface BaseResponseBoolean
 */
export interface BaseResponseBoolean {
    /**
     * 
     * @type {number}
     * @memberof BaseResponseBoolean
     */
    'code'?: number;
    /**
     * 
     * @type {string}
     * @memberof BaseResponseBoolean
     */
    'desc'?: string;
    /**
     * 
     * @type {boolean}
     * @memberof BaseResponseBoolean
     */
    'data'?: boolean;
}
/**
 * 
 * @export
 * @interface BaseResponseString
 */
export interface BaseResponseString {
    /**
     * 
     * @type {number}
     * @memberof BaseResponseString
     */
    'code'?: number;
    /**
     * 
     * @type {string}
     * @memberof BaseResponseString
     */
    'desc'?: string;
    /**
     * 
     * @type {string}
     * @memberof BaseResponseString
     */
    'data'?: string;
}
/**
 * 
 * @export
 * @interface BlockStatusResp
 */
export interface BlockStatusResp {
    /**
     * 
     * @type {string}
     * @memberof BlockStatusResp
     */
    'global'?: BlockStatusRespGlobalEnum;
    /**
     * 
     * @type {{ [key: string]: string; }}
     * @memberof BlockStatusResp
     */
    'named'?: { [key: string]: string; };
}

export const BlockStatusRespGlobalEnum = {
    Prepare: 'PREPARE',
    Pending: 'PENDING',
    Finished: 'FINISHED',
    Unknown: 'UNKNOWN'
} as const;

export type BlockStatusRespGlobalEnum = typeof BlockStatusRespGlobalEnum[keyof typeof BlockStatusRespGlobalEnum];
export const BlockStatusRespNamedEnum = {
    Prepare: 'PREPARE',
    Pending: 'PENDING',
    Finished: 'FINISHED',
    Unknown: 'UNKNOWN'
} as const;

export type BlockStatusRespNamedEnum = typeof BlockStatusRespNamedEnum[keyof typeof BlockStatusRespNamedEnum];

/**
 * 
 * @export
 * @interface Bound
 */
export interface Bound {
    /**
     * 
     * @type {string}
     * @memberof Bound
     */
    'id'?: string;
    /**
     * 
     * @type {string}
     * @memberof Bound
     */
    'name'?: string;
}
/**
 * 
 * @export
 * @interface Condition
 */
export interface Condition {
    /**
     * 
     * @type {string}
     * @memberof Condition
     */
    'id'?: string;
    /**
     * 
     * @type {string}
     * @memberof Condition
     */
    'opt'?: ConditionOptEnum;
    /**
     * 
     * @type {object}
     * @memberof Condition
     */
    'value'?: object;
}

export const ConditionOptEnum = {
    Eq: 'EQ',
    Neq: 'NEQ',
    Gt: 'GT',
    Gte: 'GTE',
    Lt: 'LT',
    Lte: 'LTE',
    And: 'AND',
    Or: 'OR'
} as const;

export type ConditionOptEnum = typeof ConditionOptEnum[keyof typeof ConditionOptEnum];

/**
 * 
 * @export
 * @interface CreateActivityRequest
 */
export interface CreateActivityRequest {
    /**
     * 
     * @type {string}
     * @memberof CreateActivityRequest
     */
    'name'?: string;
    /**
     * 
     * @type {string}
     * @memberof CreateActivityRequest
     */
    'description'?: string;
    /**
     * 
     * @type {LotteryPool}
     * @memberof CreateActivityRequest
     */
    'pool'?: LotteryPool;
    /**
     * 
     * @type {string}
     * @memberof CreateActivityRequest
     */
    'startAt'?: string;
    /**
     * 
     * @type {string}
     * @memberof CreateActivityRequest
     */
    'endAt'?: string;
    /**
     * 
     * @type {boolean}
     * @memberof CreateActivityRequest
     */
    'enabled'?: boolean;
    /**
     * 
     * @type {boolean}
     * @memberof CreateActivityRequest
     */
    'hidden'?: boolean;
    /**
     * 
     * @type {boolean}
     * @memberof CreateActivityRequest
     */
    'manualFinalize'?: boolean;
}
/**
 * 
 * @export
 * @interface CreateAdminRequest
 */
export interface CreateAdminRequest {
    /**
     * 
     * @type {string}
     * @memberof CreateAdminRequest
     */
    'email'?: string;
}
/**
 * 创建人拉人关联关系结果
 * @export
 * @interface CreateBindRelationResultVO
 */
export interface CreateBindRelationResultVO {
    /**
     * 是否成功创建人拉人关联关系。false表示只是给当前用户绑定了角色，但是因为不是第一次绑定，所以不能成功与邀请者建立人拉人联系
     * @type {boolean}
     * @memberof CreateBindRelationResultVO
     */
    'success'?: boolean;
    /**
     * 
     * @type {RoleInviteRelation}
     * @memberof CreateBindRelationResultVO
     */
    'roleInviteRelation'?: RoleInviteRelation;
}
/**
 * 
 * @export
 * @interface CreateResourceRequest
 */
export interface CreateResourceRequest {
    /**
     * 
     * @type {number}
     * @memberof CreateResourceRequest
     */
    'short'?: number;
    /**
     * 
     * @type {string}
     * @memberof CreateResourceRequest
     */
    'char'?: string;
    /**
     * 
     * @type {number}
     * @memberof CreateResourceRequest
     */
    'int'?: number;
    /**
     * 
     * @type {number}
     * @memberof CreateResourceRequest
     */
    'long'?: number;
    /**
     * 
     * @type {number}
     * @memberof CreateResourceRequest
     */
    'float'?: number;
    /**
     * 
     * @type {number}
     * @memberof CreateResourceRequest
     */
    'double'?: number;
    /**
     * 
     * @type {boolean}
     * @memberof CreateResourceRequest
     */
    'direct'?: boolean;
    /**
     * 
     * @type {boolean}
     * @memberof CreateResourceRequest
     */
    'readOnly'?: boolean;
}
/**
 * 
 * @export
 * @interface CreateUrlRequest
 */
export interface CreateUrlRequest {
    /**
     * 
     * @type {string}
     * @memberof CreateUrlRequest
     */
    'ssn'?: string;
    /**
     * 
     * @type {DefaultRole}
     * @memberof CreateUrlRequest
     */
    'role'?: DefaultRole;
}
/**
 * 
 * @export
 * @interface CreateUrsTokenWithRoleRequest
 */
export interface CreateUrsTokenWithRoleRequest {
    /**
     * ssn
     * @type {string}
     * @memberof CreateUrsTokenWithRoleRequest
     */
    'ssn': string;
    /**
     * 
     * @type {DefaultRole}
     * @memberof CreateUrsTokenWithRoleRequest
     */
    'role'?: DefaultRole;
}
/**
 * 累计签到配置
 * @export
 * @interface CumulativeSignInConfig
 */
export interface CumulativeSignInConfig {
    /**
     * 
     * @type {string}
     * @memberof CumulativeSignInConfig
     */
    'id'?: string;
    /**
     * 奖励列表
     * @type {Array<Reward>}
     * @memberof CumulativeSignInConfig
     */
    'rewards'?: Array<Reward>;
    /**
     * 
     * @type {string}
     * @memberof CumulativeSignInConfig
     */
    'createdAt'?: string;
    /**
     * 
     * @type {string}
     * @memberof CumulativeSignInConfig
     */
    'updatedAt'?: string;
}
/**
 * 累计签到配置更新请求
 * @export
 * @interface CumulativeSignInConfigSaveRequest
 */
export interface CumulativeSignInConfigSaveRequest {
    /**
     * 奖励列表
     * @type {Array<Reward>}
     * @memberof CumulativeSignInConfigSaveRequest
     */
    'rewards'?: Array<Reward>;
}
/**
 * 累计签到记录
 * @export
 * @interface CumulativeSignInRecord
 */
export interface CumulativeSignInRecord {
    /**
     * 
     * @type {string}
     * @memberof CumulativeSignInRecord
     */
    'id'?: string;
    /**
     * 签到日期
     * @type {string}
     * @memberof CumulativeSignInRecord
     */
    'date'?: string;
    /**
     * 角色id
     * @type {string}
     * @memberof CumulativeSignInRecord
     */
    'owner'?: string;
    /**
     * 第几次签到
     * @type {number}
     * @memberof CumulativeSignInRecord
     */
    'no'?: number;
    /**
     * 
     * @type {Reward}
     * @memberof CumulativeSignInRecord
     */
    'reward'?: Reward;
    /**
     * 发奖记录id
     * @type {string}
     * @memberof CumulativeSignInRecord
     */
    'rewardPostRecordId'?: string;
    /**
     * 
     * @type {string}
     * @memberof CumulativeSignInRecord
     */
    'createdAt'?: string;
    /**
     * 
     * @type {string}
     * @memberof CumulativeSignInRecord
     */
    'updatedAt'?: string;
    /**
     * 是否为今天的签到记录
     * @type {boolean}
     * @memberof CumulativeSignInRecord
     */
    'today'?: boolean;
}
/**
 * 
 * @export
 * @interface DailyRollCount
 */
export interface DailyRollCount {
    /**
     * 
     * @type {number}
     * @memberof DailyRollCount
     */
    'count'?: number;
    /**
     * 
     * @type {string}
     * @memberof DailyRollCount
     */
    'time'?: string;
}
/**
 * 角色信息
 * @export
 * @interface DefaultRole
 */
export interface DefaultRole {
    /**
     * 
     * @type {string}
     * @memberof DefaultRole
     */
    'hostId'?: string;
    /**
     * 
     * @type {string}
     * @memberof DefaultRole
     */
    'hostName'?: string;
    /**
     * 
     * @type {string}
     * @memberof DefaultRole
     */
    'roleId'?: string;
    /**
     * 
     * @type {string}
     * @memberof DefaultRole
     */
    'roleName'?: string;
    /**
     * 
     * @type {string}
     * @memberof DefaultRole
     */
    'avatar'?: string;
    /**
     * 
     * @type {string}
     * @memberof DefaultRole
     */
    'level'?: string;
    /**
     * 
     * @type {string}
     * @memberof DefaultRole
     */
    'createTime'?: string;
    /**
     * 
     * @type {string}
     * @memberof DefaultRole
     */
    'lastLoginTime'?: string;
    /**
     * 
     * @type {{ [key: string]: { [key: string]: any; }; }}
     * @memberof DefaultRole
     */
    'extra'?: { [key: string]: { [key: string]: any; }; };
}
/**
 * 
 * @export
 * @interface Dict
 */
export interface Dict {
    /**
     * 
     * @type {string}
     * @memberof Dict
     */
    'id'?: string;
    /**
     * 字典key
     * @type {string}
     * @memberof Dict
     */
    'key'?: string;
    /**
     * 
     * @type {object}
     * @memberof Dict
     */
    'value'?: object;
    /**
     * 值类型<br>枚举值说明：<br>STRING: 字符串;<br>OBJECT: 对象;<br>NUMBER: 数字;<br>ARRAY: 数组;<br>IMAGE: 图片
     * @type {string}
     * @memberof Dict
     */
    'type'?: DictTypeEnum;
    /**
     * 描述
     * @type {string}
     * @memberof Dict
     */
    'desc'?: string;
    /**
     * 
     * @type {string}
     * @memberof Dict
     */
    'createdAt'?: string;
    /**
     * 
     * @type {string}
     * @memberof Dict
     */
    'updatedAt'?: string;
}

export const DictTypeEnum = {
    String: 'STRING',
    Object: 'OBJECT',
    Number: 'NUMBER',
    Array: 'ARRAY',
    Image: 'IMAGE'
} as const;

export type DictTypeEnum = typeof DictTypeEnum[keyof typeof DictTypeEnum];

/**
 * 
 * @export
 * @interface DictSaveRequest
 */
export interface DictSaveRequest {
    /**
     * 字典key
     * @type {string}
     * @memberof DictSaveRequest
     */
    'key': string;
    /**
     * 
     * @type {object}
     * @memberof DictSaveRequest
     */
    'value': object;
    /**
     * 值类型<br>枚举值说明：<br>STRING: 字符串;<br>OBJECT: 对象;<br>NUMBER: 数字;<br>ARRAY: 数组;<br>IMAGE: 图片
     * @type {string}
     * @memberof DictSaveRequest
     */
    'type': DictSaveRequestTypeEnum;
    /**
     * 描述
     * @type {string}
     * @memberof DictSaveRequest
     */
    'desc'?: string;
}

export const DictSaveRequestTypeEnum = {
    String: 'STRING',
    Object: 'OBJECT',
    Number: 'NUMBER',
    Array: 'ARRAY',
    Image: 'IMAGE'
} as const;

export type DictSaveRequestTypeEnum = typeof DictSaveRequestTypeEnum[keyof typeof DictSaveRequestTypeEnum];

/**
 * 
 * @export
 * @interface ErrorDetails
 */
export interface ErrorDetails {
    /**
     * 
     * @type {string}
     * @memberof ErrorDetails
     */
    'msg'?: string;
    /**
     * 
     * @type {number}
     * @memberof ErrorDetails
     */
    'code'?: number;
    /**
     * 
     * @type {string}
     * @memberof ErrorDetails
     */
    'details'?: string;
}
/**
 * 
 * @export
 * @interface ExchangeActivity
 */
export interface ExchangeActivity {
    /**
     * 
     * @type {string}
     * @memberof ExchangeActivity
     */
    'name'?: string;
    /**
     * 
     * @type {string}
     * @memberof ExchangeActivity
     */
    'id'?: string;
    /**
     * 
     * @type {boolean}
     * @memberof ExchangeActivity
     */
    'enabled'?: boolean;
    /**
     * 
     * @type {string}
     * @memberof ExchangeActivity
     */
    'description'?: string;
    /**
     * 
     * @type {string}
     * @memberof ExchangeActivity
     */
    'startAt'?: string;
    /**
     * 
     * @type {string}
     * @memberof ExchangeActivity
     */
    'endAt'?: string;
    /**
     * 
     * @type {Array<ExchangeItem>}
     * @memberof ExchangeActivity
     */
    'items'?: Array<ExchangeItem>;
}
/**
 * 
 * @export
 * @interface ExchangeItem
 */
export interface ExchangeItem {
    /**
     * 
     * @type {string}
     * @memberof ExchangeItem
     */
    'itemId'?: string;
    /**
     * 
     * @type {string}
     * @memberof ExchangeItem
     */
    'type'?: string;
    /**
     * 
     * @type {string}
     * @memberof ExchangeItem
     */
    'name'?: string;
    /**
     * 
     * @type {string}
     * @memberof ExchangeItem
     */
    'description'?: string;
    /**
     * 
     * @type {{ [key: string]: number; }}
     * @memberof ExchangeItem
     */
    'pointCosts'?: { [key: string]: number; };
    /**
     * 
     * @type {number}
     * @memberof ExchangeItem
     */
    'stock'?: number;
    /**
     * 
     * @type {number}
     * @memberof ExchangeItem
     */
    'remainStock'?: number;
    /**
     * 
     * @type {{ [key: string]: number; }}
     * @memberof ExchangeItem
     */
    'bounds'?: { [key: string]: number; };
}
/**
 * 
 * @export
 * @interface ExchangeRecord
 */
export interface ExchangeRecord {
    /**
     * 
     * @type {string}
     * @memberof ExchangeRecord
     */
    'id'?: string;
    /**
     * 
     * @type {string}
     * @memberof ExchangeRecord
     */
    'itemId'?: string;
    /**
     * 
     * @type {string}
     * @memberof ExchangeRecord
     */
    'name'?: string;
    /**
     * 
     * @type {string}
     * @memberof ExchangeRecord
     */
    'type'?: string;
    /**
     * 
     * @type {string}
     * @memberof ExchangeRecord
     */
    'description'?: string;
    /**
     * 
     * @type {Address}
     * @memberof ExchangeRecord
     */
    'address'?: Address;
    /**
     * 
     * @type {boolean}
     * @memberof ExchangeRecord
     */
    'addressEditable'?: boolean;
    /**
     * 
     * @type {string}
     * @memberof ExchangeRecord
     */
    'createdAt'?: string;
    /**
     * 
     * @type {string}
     * @memberof ExchangeRecord
     */
    'updatedAt'?: string;
}
/**
 * 
 * @export
 * @interface Feedback
 */
export interface Feedback {
    /**
     * id
     * @type {string}
     * @memberof Feedback
     */
    'id'?: string;
    /**
     * 角色id
     * @type {string}
     * @memberof Feedback
     */
    'owner'?: string;
    /**
     * 角色名称
     * @type {string}
     * @memberof Feedback
     */
    'roleName'?: string;
    /**
     * 服务器id
     * @type {string}
     * @memberof Feedback
     */
    'hostId'?: string;
    /**
     * 服务器名称
     * @type {string}
     * @memberof Feedback
     */
    'hostName'?: string;
    /**
     * 微信unionId
     * @type {string}
     * @memberof Feedback
     */
    'unionId'?: string;
    /**
     * 微信openId
     * @type {string}
     * @memberof Feedback
     */
    'openId'?: string;
    /**
     * 内容
     * @type {string}
     * @memberof Feedback
     */
    'content'?: string;
    /**
     * 手机号
     * @type {string}
     * @memberof Feedback
     */
    'phone'?: string;
    /**
     * 图片列表。最多6张
     * @type {Array<string>}
     * @memberof Feedback
     */
    'images'?: Array<string>;
    /**
     * 创建时间
     * @type {string}
     * @memberof Feedback
     */
    'createdAt'?: string;
    /**
     * 更新时间
     * @type {string}
     * @memberof Feedback
     */
    'updatedAt'?: string;
}
/**
 * 意见反馈创建请求
 * @export
 * @interface FeedbackCreateRequest
 */
export interface FeedbackCreateRequest {
    /**
     * 内容
     * @type {string}
     * @memberof FeedbackCreateRequest
     */
    'content': string;
    /**
     * 手机号
     * @type {string}
     * @memberof FeedbackCreateRequest
     */
    'phone'?: string;
    /**
     * 图片列表，最多6张
     * @type {Array<string>}
     * @memberof FeedbackCreateRequest
     */
    'images'?: Array<string>;
}
/**
 * 
 * @export
 * @interface LotteryActivity
 */
export interface LotteryActivity {
    /**
     * 
     * @type {string}
     * @memberof LotteryActivity
     */
    'id'?: string;
    /**
     * 
     * @type {string}
     * @memberof LotteryActivity
     */
    'createdAt'?: string;
    /**
     * 
     * @type {string}
     * @memberof LotteryActivity
     */
    'updatedAt'?: string;
    /**
     * 
     * @type {string}
     * @memberof LotteryActivity
     */
    'name'?: string;
    /**
     * 
     * @type {string}
     * @memberof LotteryActivity
     */
    'description'?: string;
    /**
     * 
     * @type {LotteryPool}
     * @memberof LotteryActivity
     */
    'pool'?: LotteryPool;
    /**
     * 
     * @type {string}
     * @memberof LotteryActivity
     */
    'startAt'?: string;
    /**
     * 
     * @type {string}
     * @memberof LotteryActivity
     */
    'endAt'?: string;
    /**
     * 
     * @type {boolean}
     * @memberof LotteryActivity
     */
    'enabled'?: boolean;
    /**
     * 
     * @type {boolean}
     * @memberof LotteryActivity
     */
    'hidden'?: boolean;
    /**
     * 
     * @type {boolean}
     * @memberof LotteryActivity
     */
    'manualFinalize'?: boolean;
    /**
     * 
     * @type {boolean}
     * @memberof LotteryActivity
     */
    'activated'?: boolean;
}
/**
 * 
 * @export
 * @interface LotteryCost
 */
export interface LotteryCost {
    /**
     * 
     * @type {string}
     * @memberof LotteryCost
     */
    'pointId'?: string;
    /**
     * 
     * @type {number}
     * @memberof LotteryCost
     */
    'amount'?: number;
}
/**
 * 
 * @export
 * @interface LotteryDynamicProbability
 */
export interface LotteryDynamicProbability {
    /**
     * 
     * @type {string}
     * @memberof LotteryDynamicProbability
     */
    'name'?: string;
    /**
     * 
     * @type {Array<Condition>}
     * @memberof LotteryDynamicProbability
     */
    'conditions'?: Array<Condition>;
    /**
     * 
     * @type {{ [key: string]: number; }}
     * @memberof LotteryDynamicProbability
     */
    'values'?: { [key: string]: number; };
}
/**
 * 
 * @export
 * @interface LotteryExchangeActivity
 */
export interface LotteryExchangeActivity {
    /**
     * 
     * @type {string}
     * @memberof LotteryExchangeActivity
     */
    'id'?: string;
    /**
     * 
     * @type {string}
     * @memberof LotteryExchangeActivity
     */
    'name'?: string;
    /**
     * 
     * @type {string}
     * @memberof LotteryExchangeActivity
     */
    'description'?: string;
    /**
     * 
     * @type {string}
     * @memberof LotteryExchangeActivity
     */
    'startAt'?: string;
    /**
     * 
     * @type {string}
     * @memberof LotteryExchangeActivity
     */
    'endAt'?: string;
    /**
     * 
     * @type {boolean}
     * @memberof LotteryExchangeActivity
     */
    'enabled'?: boolean;
    /**
     * 
     * @type {Array<ExchangeItem>}
     * @memberof LotteryExchangeActivity
     */
    'items'?: Array<ExchangeItem>;
    /**
     * 
     * @type {string}
     * @memberof LotteryExchangeActivity
     */
    'createdAt'?: string;
    /**
     * 
     * @type {string}
     * @memberof LotteryExchangeActivity
     */
    'updatedAt'?: string;
    /**
     * 
     * @type {boolean}
     * @memberof LotteryExchangeActivity
     */
    'valid'?: boolean;
}
/**
 * 
 * @export
 * @interface LotteryPool
 */
export interface LotteryPool {
    /**
     * 
     * @type {Array<LotteryProduct>}
     * @memberof LotteryPool
     */
    'items'?: Array<LotteryProduct>;
    /**
     * 
     * @type {Array<LotteryPoolRule>}
     * @memberof LotteryPool
     */
    'rules'?: Array<LotteryPoolRule>;
    /**
     * 
     * @type {Array<LotteryPoolBound>}
     * @memberof LotteryPool
     */
    'bounds'?: Array<LotteryPoolBound>;
    /**
     * 
     * @type {Array<LotteryDynamicProbability>}
     * @memberof LotteryPool
     */
    'probabilities'?: Array<LotteryDynamicProbability>;
    /**
     * 
     * @type {boolean}
     * @memberof LotteryPool
     */
    'completeAllProbabilities'?: boolean;
    /**
     * 
     * @type {Array<Condition>}
     * @memberof LotteryPool
     */
    'conditions'?: Array<Condition>;
    /**
     * 
     * @type {LotteryCost}
     * @memberof LotteryPool
     */
    'cost'?: LotteryCost;
    /**
     * 
     * @type {Array<LotteryCost>}
     * @memberof LotteryPool
     */
    'costs'?: Array<LotteryCost>;
    /**
     * 
     * @type {Strategy}
     * @memberof LotteryPool
     */
    'outOfTotalStrategy'?: Strategy;
}
/**
 * 
 * @export
 * @interface LotteryPoolBound
 */
export interface LotteryPoolBound {
    /**
     * 
     * @type {string}
     * @memberof LotteryPoolBound
     */
    'id'?: string;
    /**
     * 
     * @type {string}
     * @memberof LotteryPoolBound
     */
    'name'?: string;
    /**
     * 
     * @type {string}
     * @memberof LotteryPoolBound
     */
    'bound'?: string;
    /**
     * 
     * @type {Set<string>}
     * @memberof LotteryPoolBound
     */
    'targets'?: Set<string>;
    /**
     * 
     * @type {number}
     * @memberof LotteryPoolBound
     */
    'limit'?: number;
    /**
     * 
     * @type {Strategy}
     * @memberof LotteryPoolBound
     */
    'strategy'?: Strategy;
}
/**
 * 
 * @export
 * @interface LotteryPoolRule
 */
export interface LotteryPoolRule {
    /**
     * 
     * @type {string}
     * @memberof LotteryPoolRule
     */
    'name'?: string;
    /**
     * 
     * @type {Array<Condition>}
     * @memberof LotteryPoolRule
     */
    'conditions'?: Array<Condition>;
    /**
     * 
     * @type {Set<string>}
     * @memberof LotteryPoolRule
     */
    'targets'?: Set<string>;
    /**
     * 
     * @type {Strategy}
     * @memberof LotteryPoolRule
     */
    'strategy'?: Strategy;
}
/**
 * 
 * @export
 * @interface LotteryProduct
 */
export interface LotteryProduct {
    /**
     * 
     * @type {string}
     * @memberof LotteryProduct
     */
    'id'?: string;
    /**
     * 
     * @type {string}
     * @memberof LotteryProduct
     */
    'name'?: string;
    /**
     * 
     * @type {string}
     * @memberof LotteryProduct
     */
    'description'?: string;
    /**
     * 
     * @type {string}
     * @memberof LotteryProduct
     */
    'type'?: string;
    /**
     * 数量或金额（单位：分）
     * @type {number}
     * @memberof LotteryProduct
     */
    'amount'?: number;
    /**
     * 
     * @type {{ [key: string]: { [key: string]: any; }; }}
     * @memberof LotteryProduct
     */
    'extra'?: { [key: string]: { [key: string]: any; }; };
    /**
     * 内部使用的extra
     * @type {{ [key: string]: { [key: string]: any; }; }}
     * @memberof LotteryProduct
     */
    'innerExtra'?: { [key: string]: { [key: string]: any; }; };
    /**
     * 
     * @type {number}
     * @memberof LotteryProduct
     */
    'probability'?: number;
    /**
     * 
     * @type {number}
     * @memberof LotteryProduct
     */
    'total'?: number;
}
/**
 * 
 * @export
 * @interface NewFileResponse
 */
export interface NewFileResponse {
    /**
     * 
     * @type {string}
     * @memberof NewFileResponse
     */
    'url'?: string;
    /**
     * 
     * @type {string}
     * @memberof NewFileResponse
     */
    'mime'?: string;
    /**
     * 
     * @type {Array<number>}
     * @memberof NewFileResponse
     */
    'picSize'?: Array<number>;
    /**
     * 
     * @type {string}
     * @memberof NewFileResponse
     */
    'ping'?: string;
    /**
     * 
     * @type {Array<Array<any>>}
     * @memberof NewFileResponse
     */
    'color'?: Array<Array<any>>;
    /**
     * 
     * @type {string}
     * @memberof NewFileResponse
     */
    'videoCover'?: string;
    /**
     * 
     * @type {number}
     * @memberof NewFileResponse
     */
    'fsize'?: number;
    /**
     * 
     * @type {string}
     * @memberof NewFileResponse
     */
    'md5'?: string;
}
/**
 * 通知任务
 * @export
 * @interface NotifyTask
 */
export interface NotifyTask {
    /**
     * 
     * @type {string}
     * @memberof NotifyTask
     */
    'id'?: string;
    /**
     * 任务类型<br>枚举值说明：<br>CUMULATIVE_SIGN_IN: 累计签到;<br>SCORE_EXPIRE: 积分到期
     * @type {string}
     * @memberof NotifyTask
     */
    'type'?: NotifyTaskTypeEnum;
    /**
     * 消息发送日期。用于建立唯一索引，防止重复发送
     * @type {string}
     * @memberof NotifyTask
     */
    'date'?: string;
    /**
     * 角色id
     * @type {string}
     * @memberof NotifyTask
     */
    'owner'?: string;
    /**
     * 微信openid
     * @type {string}
     * @memberof NotifyTask
     */
    'openId'?: string;
    /**
     * 微信unionid
     * @type {string}
     * @memberof NotifyTask
     */
    'unionId'?: string;
    /**
     * 消息模板id
     * @type {string}
     * @memberof NotifyTask
     */
    'templateId'?: string;
    /**
     * 状态<br>枚举值说明：<br>INITIAL: 初始;<br>IN_PROGRESS: 进行中;<br>SUCCESS: 成功;<br>FAILURE: 失败
     * @type {string}
     * @memberof NotifyTask
     */
    'status'?: NotifyTaskStatusEnum;
    /**
     * 微信错误码
     * @type {number}
     * @memberof NotifyTask
     */
    'wxErrcode'?: number;
    /**
     * 微信错误消息
     * @type {string}
     * @memberof NotifyTask
     */
    'wxErrmsg'?: string;
    /**
     * 错误消息
     * @type {string}
     * @memberof NotifyTask
     */
    'errmsg'?: string;
    /**
     * 
     * @type {string}
     * @memberof NotifyTask
     */
    'createdAt'?: string;
    /**
     * 
     * @type {string}
     * @memberof NotifyTask
     */
    'updatedAt'?: string;
}

export const NotifyTaskTypeEnum = {
    CumulativeSignIn: 'CUMULATIVE_SIGN_IN',
    ScoreExpire: 'SCORE_EXPIRE'
} as const;

export type NotifyTaskTypeEnum = typeof NotifyTaskTypeEnum[keyof typeof NotifyTaskTypeEnum];
export const NotifyTaskStatusEnum = {
    Initial: 'INITIAL',
    InProgress: 'IN_PROGRESS',
    Success: 'SUCCESS',
    Failure: 'FAILURE'
} as const;

export type NotifyTaskStatusEnum = typeof NotifyTaskStatusEnum[keyof typeof NotifyTaskStatusEnum];

/**
 * 累计签到通知任务创建请求
 * @export
 * @interface NotifyTaskCreateRequest
 */
export interface NotifyTaskCreateRequest {
    /**
     * 消息模板id
     * @type {string}
     * @memberof NotifyTaskCreateRequest
     */
    'templateId': string;
}
/**
 * 
 * @export
 * @interface PageFeedback
 */
export interface PageFeedback {
    /**
     * 
     * @type {number}
     * @memberof PageFeedback
     */
    'totalPages'?: number;
    /**
     * 
     * @type {number}
     * @memberof PageFeedback
     */
    'totalElements'?: number;
    /**
     * 
     * @type {number}
     * @memberof PageFeedback
     */
    'size'?: number;
    /**
     * 
     * @type {Array<Feedback>}
     * @memberof PageFeedback
     */
    'content'?: Array<Feedback>;
    /**
     * 
     * @type {number}
     * @memberof PageFeedback
     */
    'number'?: number;
    /**
     * 
     * @type {SortObject}
     * @memberof PageFeedback
     */
    'sort'?: SortObject;
    /**
     * 
     * @type {PageableObject}
     * @memberof PageFeedback
     */
    'pageable'?: PageableObject;
    /**
     * 
     * @type {number}
     * @memberof PageFeedback
     */
    'numberOfElements'?: number;
    /**
     * 
     * @type {boolean}
     * @memberof PageFeedback
     */
    'first'?: boolean;
    /**
     * 
     * @type {boolean}
     * @memberof PageFeedback
     */
    'last'?: boolean;
    /**
     * 
     * @type {boolean}
     * @memberof PageFeedback
     */
    'empty'?: boolean;
}
/**
 * 
 * @export
 * @interface PagePost
 */
export interface PagePost {
    /**
     * 
     * @type {number}
     * @memberof PagePost
     */
    'totalPages'?: number;
    /**
     * 
     * @type {number}
     * @memberof PagePost
     */
    'totalElements'?: number;
    /**
     * 
     * @type {number}
     * @memberof PagePost
     */
    'size'?: number;
    /**
     * 
     * @type {Array<Post>}
     * @memberof PagePost
     */
    'content'?: Array<Post>;
    /**
     * 
     * @type {number}
     * @memberof PagePost
     */
    'number'?: number;
    /**
     * 
     * @type {SortObject}
     * @memberof PagePost
     */
    'sort'?: SortObject;
    /**
     * 
     * @type {PageableObject}
     * @memberof PagePost
     */
    'pageable'?: PageableObject;
    /**
     * 
     * @type {number}
     * @memberof PagePost
     */
    'numberOfElements'?: number;
    /**
     * 
     * @type {boolean}
     * @memberof PagePost
     */
    'first'?: boolean;
    /**
     * 
     * @type {boolean}
     * @memberof PagePost
     */
    'last'?: boolean;
    /**
     * 
     * @type {boolean}
     * @memberof PagePost
     */
    'empty'?: boolean;
}
/**
 * 
 * @export
 * @interface PagePostUserRelation
 */
export interface PagePostUserRelation {
    /**
     * 
     * @type {number}
     * @memberof PagePostUserRelation
     */
    'totalPages'?: number;
    /**
     * 
     * @type {number}
     * @memberof PagePostUserRelation
     */
    'totalElements'?: number;
    /**
     * 
     * @type {number}
     * @memberof PagePostUserRelation
     */
    'size'?: number;
    /**
     * 
     * @type {Array<PostUserRelation>}
     * @memberof PagePostUserRelation
     */
    'content'?: Array<PostUserRelation>;
    /**
     * 
     * @type {number}
     * @memberof PagePostUserRelation
     */
    'number'?: number;
    /**
     * 
     * @type {SortObject}
     * @memberof PagePostUserRelation
     */
    'sort'?: SortObject;
    /**
     * 
     * @type {PageableObject}
     * @memberof PagePostUserRelation
     */
    'pageable'?: PageableObject;
    /**
     * 
     * @type {number}
     * @memberof PagePostUserRelation
     */
    'numberOfElements'?: number;
    /**
     * 
     * @type {boolean}
     * @memberof PagePostUserRelation
     */
    'first'?: boolean;
    /**
     * 
     * @type {boolean}
     * @memberof PagePostUserRelation
     */
    'last'?: boolean;
    /**
     * 
     * @type {boolean}
     * @memberof PagePostUserRelation
     */
    'empty'?: boolean;
}
/**
 * 
 * @export
 * @interface PageableObject
 */
export interface PageableObject {
    /**
     * 
     * @type {number}
     * @memberof PageableObject
     */
    'offset'?: number;
    /**
     * 
     * @type {SortObject}
     * @memberof PageableObject
     */
    'sort'?: SortObject;
    /**
     * 
     * @type {number}
     * @memberof PageableObject
     */
    'pageNumber'?: number;
    /**
     * 
     * @type {number}
     * @memberof PageableObject
     */
    'pageSize'?: number;
    /**
     * 
     * @type {boolean}
     * @memberof PageableObject
     */
    'paged'?: boolean;
    /**
     * 
     * @type {boolean}
     * @memberof PageableObject
     */
    'unpaged'?: boolean;
}
/**
 * 帖子
 * @export
 * @interface Post
 */
export interface Post {
    /**
     * id
     * @type {string}
     * @memberof Post
     */
    'id'?: string;
    /**
     * 标题
     * @type {string}
     * @memberof Post
     */
    'title'?: string;
    /**
     * 内容
     * @type {string}
     * @memberof Post
     */
    'content'?: string;
    /**
     * 帖子类型<br>枚举值说明：<br>ARTICLE: 文章;<br>VIDEO: 视频
     * @type {string}
     * @memberof Post
     */
    'type'?: PostTypeEnum;
    /**
     * 封面
     * @type {string}
     * @memberof Post
     */
    'cover'?: string;
    /**
     * 视频地址
     * @type {string}
     * @memberof Post
     */
    'videoUrl'?: string;
    /**
     * 发布时间
     * @type {string}
     * @memberof Post
     */
    'publishAt'?: string;
    /**
     * 是否可见
     * @type {boolean}
     * @memberof Post
     */
    'visible'?: boolean;
    /**
     * 作者id
     * @type {string}
     * @memberof Post
     */
    'authorId'?: string;
    /**
     * 
     * @type {PostAuthor}
     * @memberof Post
     */
    'author'?: PostAuthor;
    /**
     * 一级标签id
     * @type {string}
     * @memberof Post
     */
    'level1TagId'?: string;
    /**
     * 一级标签名称
     * @type {string}
     * @memberof Post
     */
    'level1TagName'?: string;
    /**
     * 二级标签id
     * @type {string}
     * @memberof Post
     */
    'level2TagId'?: string;
    /**
     * 二级标签名称
     * @type {string}
     * @memberof Post
     */
    'level2TagName'?: string;
    /**
     * 实际浏览量
     * @type {number}
     * @memberof Post
     */
    'viewCount'?: number;
    /**
     * 实际转发量
     * @type {number}
     * @memberof Post
     */
    'forwardCount'?: number;
    /**
     * 实际点赞量
     * @type {number}
     * @memberof Post
     */
    'likeCount'?: number;
    /**
     * 实际收藏量
     * @type {number}
     * @memberof Post
     */
    'collectCount'?: number;
    /**
     * 前台展示用的虚假浏览量
     * @type {number}
     * @memberof Post
     */
    'displayViewCount'?: number;
    /**
     * 实际转发量
     * @type {number}
     * @memberof Post
     */
    'displayForwardCount'?: number;
    /**
     * 前台展示用的虚假点赞量
     * @type {number}
     * @memberof Post
     */
    'displayLikeCount'?: number;
    /**
     * 前台展示用的虚假收藏量
     * @type {number}
     * @memberof Post
     */
    'displayCollectCount'?: number;
    /**
     * 创建时间
     * @type {string}
     * @memberof Post
     */
    'createdAt'?: string;
    /**
     * 更新时间
     * @type {string}
     * @memberof Post
     */
    'updatedAt'?: string;
}

export const PostTypeEnum = {
    Article: 'ARTICLE',
    Video: 'VIDEO'
} as const;

export type PostTypeEnum = typeof PostTypeEnum[keyof typeof PostTypeEnum];

/**
 * 帖子作者
 * @export
 * @interface PostAuthor
 */
export interface PostAuthor {
    /**
     * id
     * @type {string}
     * @memberof PostAuthor
     */
    'id'?: string;
    /**
     * 用户名称
     * @type {string}
     * @memberof PostAuthor
     */
    'name'?: string;
    /**
     * 头像名称
     * @type {string}
     * @memberof PostAuthor
     */
    'avatar'?: string;
    /**
     * 创建时间
     * @type {string}
     * @memberof PostAuthor
     */
    'createdAt'?: string;
    /**
     * 更新时间
     * @type {string}
     * @memberof PostAuthor
     */
    'updatedAt'?: string;
}
/**
 * 帖子作者保存请求
 * @export
 * @interface PostAuthorSaveRequest
 */
export interface PostAuthorSaveRequest {
    /**
     * 用户名称
     * @type {string}
     * @memberof PostAuthorSaveRequest
     */
    'name': string;
    /**
     * 头像
     * @type {string}
     * @memberof PostAuthorSaveRequest
     */
    'avatar'?: string;
}
/**
 * 帖子创建请求
 * @export
 * @interface PostCreateRequest
 */
export interface PostCreateRequest {
    /**
     * 标题
     * @type {string}
     * @memberof PostCreateRequest
     */
    'title': string;
    /**
     * 内容
     * @type {string}
     * @memberof PostCreateRequest
     */
    'content': string;
    /**
     * 帖子类型<br>枚举值说明：<br>ARTICLE: 文章;<br>VIDEO: 视频
     * @type {string}
     * @memberof PostCreateRequest
     */
    'type': PostCreateRequestTypeEnum;
    /**
     * 封面
     * @type {string}
     * @memberof PostCreateRequest
     */
    'cover'?: string;
    /**
     * 视频地址
     * @type {string}
     * @memberof PostCreateRequest
     */
    'videoUrl'?: string;
    /**
     * 发布时间
     * @type {string}
     * @memberof PostCreateRequest
     */
    'publishAt'?: string;
    /**
     * 是否可见
     * @type {boolean}
     * @memberof PostCreateRequest
     */
    'visible': boolean;
    /**
     * 作者id
     * @type {string}
     * @memberof PostCreateRequest
     */
    'authorId': string;
    /**
     * 二级标签id
     * @type {string}
     * @memberof PostCreateRequest
     */
    'level2TagId': string;
}

export const PostCreateRequestTypeEnum = {
    Article: 'ARTICLE',
    Video: 'VIDEO'
} as const;

export type PostCreateRequestTypeEnum = typeof PostCreateRequestTypeEnum[keyof typeof PostCreateRequestTypeEnum];

/**
 * 帖子虚假数据更新请求
 * @export
 * @interface PostDisplayCountsUpdateRequest
 */
export interface PostDisplayCountsUpdateRequest {
    /**
     * 前台展示用的虚假点赞量
     * @type {number}
     * @memberof PostDisplayCountsUpdateRequest
     */
    'displayLikeCount': number;
    /**
     * 前台展示用的虚假收藏量
     * @type {number}
     * @memberof PostDisplayCountsUpdateRequest
     */
    'displayCollectCount': number;
    /**
     * 前台展示用的虚假转发量
     * @type {number}
     * @memberof PostDisplayCountsUpdateRequest
     */
    'displayForwardCount': number;
}
/**
 * 帖子统计VO
 * @export
 * @interface PostStatisticsVO
 */
export interface PostStatisticsVO {
    /**
     * 文章总数
     * @type {number}
     * @memberof PostStatisticsVO
     */
    'articleCount'?: number;
    /**
     * 视频总数
     * @type {number}
     * @memberof PostStatisticsVO
     */
    'videoCount'?: number;
    /**
     * 总浏览量
     * @type {number}
     * @memberof PostStatisticsVO
     */
    'totalViewCount'?: number;
    /**
     * 总点赞量
     * @type {number}
     * @memberof PostStatisticsVO
     */
    'totalLikeCount'?: number;
    /**
     * 总收藏量
     * @type {number}
     * @memberof PostStatisticsVO
     */
    'totalCollectCount'?: number;
    /**
     * 总转发量
     * @type {number}
     * @memberof PostStatisticsVO
     */
    'totalForwardCount'?: number;
}
/**
 * 帖子标签
 * @export
 * @interface PostTag
 */
export interface PostTag {
    /**
     * id
     * @type {string}
     * @memberof PostTag
     */
    'id'?: string;
    /**
     * 用户名称
     * @type {string}
     * @memberof PostTag
     */
    'name'?: string;
    /**
     * 标签层级
     * @type {number}
     * @memberof PostTag
     */
    'level'?: number;
    /**
     * 父级标签id
     * @type {string}
     * @memberof PostTag
     */
    'parentId'?: string;
    /**
     * 子标签
     * @type {Array<PostTag>}
     * @memberof PostTag
     */
    'subTags'?: Array<PostTag>;
    /**
     * 帖子数量
     * @type {number}
     * @memberof PostTag
     */
    'postCount'?: number;
    /**
     * 创建时间
     * @type {string}
     * @memberof PostTag
     */
    'createdAt'?: string;
    /**
     * 更新时间
     * @type {string}
     * @memberof PostTag
     */
    'updatedAt'?: string;
}
/**
 * 帖子标签创建请求
 * @export
 * @interface PostTagCreateRequest
 */
export interface PostTagCreateRequest {
    /**
     * 标签名称
     * @type {string}
     * @memberof PostTagCreateRequest
     */
    'name': string;
    /**
     * 父级标签id，一级标签不需要传
     * @type {string}
     * @memberof PostTagCreateRequest
     */
    'parentId'?: string;
}
/**
 * 帖子标签更新请求
 * @export
 * @interface PostTagUpdateRequest
 */
export interface PostTagUpdateRequest {
    /**
     * 标签名称
     * @type {string}
     * @memberof PostTagUpdateRequest
     */
    'name': string;
}
/**
 * 帖子更新请求
 * @export
 * @interface PostUpdateRequest
 */
export interface PostUpdateRequest {
    /**
     * 标题
     * @type {string}
     * @memberof PostUpdateRequest
     */
    'title': string;
    /**
     * 内容
     * @type {string}
     * @memberof PostUpdateRequest
     */
    'content': string;
    /**
     * 封面
     * @type {string}
     * @memberof PostUpdateRequest
     */
    'cover'?: string;
    /**
     * 视频地址
     * @type {string}
     * @memberof PostUpdateRequest
     */
    'videoUrl'?: string;
    /**
     * 发布时间
     * @type {string}
     * @memberof PostUpdateRequest
     */
    'publishAt'?: string;
    /**
     * 是否可见
     * @type {boolean}
     * @memberof PostUpdateRequest
     */
    'visible': boolean;
    /**
     * 作者id
     * @type {string}
     * @memberof PostUpdateRequest
     */
    'authorId': string;
    /**
     * 二级标签id
     * @type {string}
     * @memberof PostUpdateRequest
     */
    'level2TagId': string;
}
/**
 * 帖子用户关联
 * @export
 * @interface PostUserRelation
 */
export interface PostUserRelation {
    /**
     * id
     * @type {string}
     * @memberof PostUserRelation
     */
    'id'?: string;
    /**
     * 角色id
     * @type {string}
     * @memberof PostUserRelation
     */
    'owner'?: string;
    /**
     * 帖子id
     * @type {string}
     * @memberof PostUserRelation
     */
    'postId'?: string;
    /**
     * 类型<br>枚举值说明：<br>LIKE: 点赞;<br>COLLECT: 收藏
     * @type {string}
     * @memberof PostUserRelation
     */
    'type'?: PostUserRelationTypeEnum;
    /**
     * 创建时间
     * @type {string}
     * @memberof PostUserRelation
     */
    'createdAt'?: string;
    /**
     * 更新时间
     * @type {string}
     * @memberof PostUserRelation
     */
    'updatedAt'?: string;
    /**
     * 
     * @type {Post}
     * @memberof PostUserRelation
     */
    'post'?: Post;
}

export const PostUserRelationTypeEnum = {
    Like: 'LIKE',
    Collect: 'COLLECT'
} as const;

export type PostUserRelationTypeEnum = typeof PostUserRelationTypeEnum[keyof typeof PostUserRelationTypeEnum];

/**
 * 帖子用户关联变更请求
 * @export
 * @interface PostUserRelationChangeRequest
 */
export interface PostUserRelationChangeRequest {
    /**
     * 帖子ID
     * @type {string}
     * @memberof PostUserRelationChangeRequest
     */
    'postId': string;
    /**
     * 关联类型<br>枚举值说明：<br>LIKE: 点赞;<br>COLLECT: 收藏
     * @type {string}
     * @memberof PostUserRelationChangeRequest
     */
    'type': PostUserRelationChangeRequestTypeEnum;
}

export const PostUserRelationChangeRequestTypeEnum = {
    Like: 'LIKE',
    Collect: 'COLLECT'
} as const;

export type PostUserRelationChangeRequestTypeEnum = typeof PostUserRelationChangeRequestTypeEnum[keyof typeof PostUserRelationChangeRequestTypeEnum];

/**
 * 帖子可见性更新请求
 * @export
 * @interface PostVisibleUpdateRequest
 */
export interface PostVisibleUpdateRequest {
    /**
     * 是否可见
     * @type {boolean}
     * @memberof PostVisibleUpdateRequest
     */
    'visible': boolean;
}
/**
 * 
 * @export
 * @interface ProductType
 */
export interface ProductType {
    /**
     * 
     * @type {string}
     * @memberof ProductType
     */
    'name'?: string;
    /**
     * 
     * @type {string}
     * @memberof ProductType
     */
    'id'?: string;
    /**
     * 
     * @type {boolean}
     * @memberof ProductType
     */
    'addressable'?: boolean;
}
/**
 * 
 * @export
 * @interface PublicLotteryItem
 */
export interface PublicLotteryItem {
    /**
     * 
     * @type {string}
     * @memberof PublicLotteryItem
     */
    'name'?: string;
    /**
     * 
     * @type {string}
     * @memberof PublicLotteryItem
     */
    'id'?: string;
    /**
     * 
     * @type {string}
     * @memberof PublicLotteryItem
     */
    'type'?: string;
    /**
     * 
     * @type {{ [key: string]: { [key: string]: any; }; }}
     * @memberof PublicLotteryItem
     */
    'extra'?: { [key: string]: { [key: string]: any; }; };
    /**
     * 
     * @type {string}
     * @memberof PublicLotteryItem
     */
    'productId'?: string;
    /**
     * 
     * @type {string}
     * @memberof PublicLotteryItem
     */
    'description'?: string;
}
/**
 * 
 * @export
 * @interface Resource
 */
export interface Resource {
    /**
     * 
     * @type {string}
     * @memberof Resource
     */
    'description'?: string;
    /**
     * 
     * @type {string}
     * @memberof Resource
     */
    'title'?: string;
    /**
     * 
     * @type {number}
     * @memberof Resource
     */
    'review'?: number;
    /**
     * 
     * @type {NewFileResponse}
     * @memberof Resource
     */
    'detail'?: NewFileResponse;
    /**
     * 
     * @type {string}
     * @memberof Resource
     */
    'id'?: string;
    /**
     * 
     * @type {string}
     * @memberof Resource
     */
    'createdAt'?: string;
    /**
     * 
     * @type {string}
     * @memberof Resource
     */
    'updatedAt'?: string;
}
/**
 * 签到奖励
 * @export
 * @interface Reward
 */
export interface Reward {
    /**
     * 奖励名称
     * @type {string}
     * @memberof Reward
     */
    'name': string;
    /**
     * 奖励图片
     * @type {string}
     * @memberof Reward
     */
    'img': string;
    /**
     * 奖励描述
     * @type {string}
     * @memberof Reward
     */
    'desc'?: string;
    /**
     * 游戏道具id
     * @type {string}
     * @memberof Reward
     */
    'rewardId': string;
}
/**
 * 
 * @export
 * @interface RoleActivenessSaveRequest
 */
export interface RoleActivenessSaveRequest {
    /**
     * 角色id
     * @type {string}
     * @memberof RoleActivenessSaveRequest
     */
    'roleId': string;
    /**
     * 活跃度日期，格式为 yyyy-MM-dd
     * @type {string}
     * @memberof RoleActivenessSaveRequest
     */
    'date': string;
    /**
     * 活跃度
     * @type {number}
     * @memberof RoleActivenessSaveRequest
     */
    'activeness': number;
}
/**
 * 角色基础信息
 * @export
 * @interface RoleBaseInfoVO
 */
export interface RoleBaseInfoVO {
    /**
     * 服务器id
     * @type {string}
     * @memberof RoleBaseInfoVO
     */
    'hostId'?: string;
    /**
     * 服务器名称
     * @type {string}
     * @memberof RoleBaseInfoVO
     */
    'hostName'?: string;
    /**
     * 角色id
     * @type {string}
     * @memberof RoleBaseInfoVO
     */
    'roleId'?: string;
    /**
     * 角色名称
     * @type {string}
     * @memberof RoleBaseInfoVO
     */
    'roleName'?: string;
    /**
     * 角色头像
     * @type {string}
     * @memberof RoleBaseInfoVO
     */
    'avatar'?: string;
    /**
     * 小程序码url
     * @type {string}
     * @memberof RoleBaseInfoVO
     */
    'qrCodeUrl'?: string;
}
/**
 * 人拉人角色关联关系
 * @export
 * @interface RoleInviteRelation
 */
export interface RoleInviteRelation {
    /**
     * ID
     * @type {string}
     * @memberof RoleInviteRelation
     */
    'id'?: string;
    /**
     * 邀请人角色id
     * @type {string}
     * @memberof RoleInviteRelation
     */
    'owner'?: string;
    /**
     * 助力人角色id
     * @type {string}
     * @memberof RoleInviteRelation
     */
    'helper'?: string;
    /**
     * 达标时的日期
     * @type {string}
     * @memberof RoleInviteRelation
     */
    'date'?: string;
    /**
     * 达标时的活跃度
     * @type {number}
     * @memberof RoleInviteRelation
     */
    'activeness'?: number;
    /**
     * 是第几个奖励
     * @type {number}
     * @memberof RoleInviteRelation
     */
    'rewardIndex'?: number;
    /**
     * 状态<br>枚举值说明：<br>UNAVAILABLE: 不可领取;<br>AVAILABLE: 可领取;<br>RECEIVED: 已领取
     * @type {string}
     * @memberof RoleInviteRelation
     */
    'status'?: RoleInviteRelationStatusEnum;
    /**
     * 创建时间
     * @type {string}
     * @memberof RoleInviteRelation
     */
    'createdAt'?: string;
    /**
     * 更新时间
     * @type {string}
     * @memberof RoleInviteRelation
     */
    'updatedAt'?: string;
}

export const RoleInviteRelationStatusEnum = {
    Unavailable: 'UNAVAILABLE',
    Available: 'AVAILABLE',
    Received: 'RECEIVED'
} as const;

export type RoleInviteRelationStatusEnum = typeof RoleInviteRelationStatusEnum[keyof typeof RoleInviteRelationStatusEnum];

/**
 * 角色邀请关系绑定请求
 * @export
 * @interface RoleInviteRelationBindRequest
 */
export interface RoleInviteRelationBindRequest {
    /**
     * 邀请人角色ID
     * @type {string}
     * @memberof RoleInviteRelationBindRequest
     */
    'inviter': string;
    /**
     * 被邀请人角色ID，从角色列表中选择
     * @type {string}
     * @memberof RoleInviteRelationBindRequest
     */
    'helper': string;
}
/**
 * 
 * @export
 * @interface SortObject
 */
export interface SortObject {
    /**
     * 
     * @type {boolean}
     * @memberof SortObject
     */
    'empty'?: boolean;
    /**
     * 
     * @type {boolean}
     * @memberof SortObject
     */
    'sorted'?: boolean;
    /**
     * 
     * @type {boolean}
     * @memberof SortObject
     */
    'unsorted'?: boolean;
}
/**
 * 
 * @export
 * @interface Strategy
 */
export interface Strategy {
    /**
     * 
     * @type {string}
     * @memberof Strategy
     */
    'type'?: StrategyTypeEnum;
    /**
     * 
     * @type {string}
     * @memberof Strategy
     */
    'target'?: string;
}

export const StrategyTypeEnum = {
    Empty: 'EMPTY',
    Roll: 'ROLL',
    Default: 'DEFAULT'
} as const;

export type StrategyTypeEnum = typeof StrategyTypeEnum[keyof typeof StrategyTypeEnum];

/**
 * 
 * @export
 * @interface TagInfo
 */
export interface TagInfo {
    /**
     * 
     * @type {string}
     * @memberof TagInfo
     */
    'id'?: string;
    /**
     * 
     * @type {string}
     * @memberof TagInfo
     */
    'title'?: string;
    /**
     * 
     * @type {string}
     * @memberof TagInfo
     */
    'type'?: TagInfoTypeEnum;
}

export const TagInfoTypeEnum = {
    Number: 'NUMBER',
    String: 'STRING',
    Boolean: 'BOOLEAN'
} as const;

export type TagInfoTypeEnum = typeof TagInfoTypeEnum[keyof typeof TagInfoTypeEnum];

/**
 * 
 * @export
 * @interface User
 */
export interface User {
    /**
     * 
     * @type {string}
     * @memberof User
     */
    'createdAt'?: string;
    /**
     * 
     * @type {string}
     * @memberof User
     */
    'updatedAt'?: string;
    /**
     * 
     * @type {string}
     * @memberof User
     */
    'id'?: string;
}
/**
 * 用户最近一次执行某个操作的标记
 * @export
 * @interface UserLastActionMark
 */
export interface UserLastActionMark {
    /**
     * id
     * @type {string}
     * @memberof UserLastActionMark
     */
    'id'?: string;
    /**
     * 所属用户
     * @type {string}
     * @memberof UserLastActionMark
     */
    'owner'?: string;
    /**
     * 操作类型<br>枚举值说明：<br>BIND_ROLE: 绑定角色
     * @type {string}
     * @memberof UserLastActionMark
     */
    'action'?: UserLastActionMarkActionEnum;
    /**
     * 创建时间
     * @type {string}
     * @memberof UserLastActionMark
     */
    'createdAt'?: string;
    /**
     * 更新时间，也就是最近1次的标记时间
     * @type {string}
     * @memberof UserLastActionMark
     */
    'updatedAt'?: string;
}

export const UserLastActionMarkActionEnum = {
    BindRole: 'BIND_ROLE'
} as const;

export type UserLastActionMarkActionEnum = typeof UserLastActionMarkActionEnum[keyof typeof UserLastActionMarkActionEnum];

/**
 * 
 * @export
 * @interface UserLotteryItem
 */
export interface UserLotteryItem {
    /**
     * 
     * @type {string}
     * @memberof UserLotteryItem
     */
    'name'?: string;
    /**
     * 
     * @type {string}
     * @memberof UserLotteryItem
     */
    'id'?: string;
    /**
     * 
     * @type {string}
     * @memberof UserLotteryItem
     */
    'type'?: string;
    /**
     * 
     * @type {Address}
     * @memberof UserLotteryItem
     */
    'address'?: Address;
    /**
     * 
     * @type {string}
     * @memberof UserLotteryItem
     */
    'owner'?: string;
    /**
     * 
     * @type {{ [key: string]: { [key: string]: any; }; }}
     * @memberof UserLotteryItem
     */
    'extra'?: { [key: string]: { [key: string]: any; }; };
    /**
     * 数量或金额（单位：分）
     * @type {number}
     * @memberof UserLotteryItem
     */
    'amount'?: number;
    /**
     * 
     * @type {string}
     * @memberof UserLotteryItem
     */
    'productId'?: string;
    /**
     * 
     * @type {string}
     * @memberof UserLotteryItem
     */
    'lotteryId'?: string;
    /**
     * 
     * @type {string}
     * @memberof UserLotteryItem
     */
    'createdAt'?: string;
    /**
     * 
     * @type {boolean}
     * @memberof UserLotteryItem
     */
    'addressEditable'?: boolean;
    /**
     * 
     * @type {boolean}
     * @memberof UserLotteryItem
     */
    'finalized'?: boolean;
    /**
     * 
     * @type {string}
     * @memberof UserLotteryItem
     */
    'finalizedAt'?: string;
    /**
     * 
     * @type {{ [key: string]: { [key: string]: any; }; }}
     * @memberof UserLotteryItem
     */
    'productExtra'?: { [key: string]: { [key: string]: any; }; };
    /**
     * 
     * @type {string}
     * @memberof UserLotteryItem
     */
    'description'?: string;
}
/**
 * 
 * @export
 * @interface UserPoint
 */
export interface UserPoint {
    /**
     * 
     * @type {string}
     * @memberof UserPoint
     */
    'id'?: string;
    /**
     * 
     * @type {string}
     * @memberof UserPoint
     */
    'createdAt'?: string;
    /**
     * 
     * @type {string}
     * @memberof UserPoint
     */
    'updatedAt'?: string;
    /**
     * 
     * @type {string}
     * @memberof UserPoint
     */
    'user'?: string;
    /**
     * 
     * @type {string}
     * @memberof UserPoint
     */
    'key'?: string;
    /**
     * 
     * @type {number}
     * @memberof UserPoint
     */
    'delta'?: number;
    /**
     * 
     * @type {number}
     * @memberof UserPoint
     */
    'point'?: number;
}
/**
 * 
 * @export
 * @interface UserPointChangeRecord
 */
export interface UserPointChangeRecord {
    /**
     * 
     * @type {string}
     * @memberof UserPointChangeRecord
     */
    'id'?: string;
    /**
     * 
     * @type {string}
     * @memberof UserPointChangeRecord
     */
    'createdAt'?: string;
    /**
     * 
     * @type {string}
     * @memberof UserPointChangeRecord
     */
    'description'?: string;
    /**
     * 
     * @type {string}
     * @memberof UserPointChangeRecord
     */
    'user'?: string;
    /**
     * 
     * @type {string}
     * @memberof UserPointChangeRecord
     */
    'key'?: string;
    /**
     * 
     * @type {string}
     * @memberof UserPointChangeRecord
     */
    'uniqueRecordKey'?: string;
    /**
     * 
     * @type {string}
     * @memberof UserPointChangeRecord
     */
    'type'?: UserPointChangeRecordTypeEnum;
    /**
     * 
     * @type {number}
     * @memberof UserPointChangeRecord
     */
    'value'?: number;
}

export const UserPointChangeRecordTypeEnum = {
    Increase: 'INCREASE',
    Decrease: 'DECREASE'
} as const;

export type UserPointChangeRecordTypeEnum = typeof UserPointChangeRecordTypeEnum[keyof typeof UserPointChangeRecordTypeEnum];

/**
 * 
 * @export
 * @interface UserPointKey
 */
export interface UserPointKey {
    /**
     * 
     * @type {string}
     * @memberof UserPointKey
     */
    'pointTitle'?: string;
    /**
     * 
     * @type {string}
     * @memberof UserPointKey
     */
    'pointKey'?: string;
}
/**
 * 
 * @export
 * @interface ValueCount
 */
export interface ValueCount {
    /**
     * 
     * @type {number}
     * @memberof ValueCount
     */
    'increase'?: number;
    /**
     * 
     * @type {number}
     * @memberof ValueCount
     */
    'decrease'?: number;
    /**
     * 
     * @type {number}
     * @memberof ValueCount
     */
    'sum'?: number;
}

/**
 * DefaultApi - axios parameter creator
 * @export
 */
export const DefaultApiAxiosParamCreator = function (configuration?: Configuration) {
    return {
        /**
         * 
         * @summary 创建意见反馈
         * @param {FeedbackCreateRequest} feedbackCreateRequest 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        createFeedbackMp: async (feedbackCreateRequest: FeedbackCreateRequest, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'feedbackCreateRequest' is not null or undefined
            assertParamExists('createFeedbackMp', 'feedbackCreateRequest', feedbackCreateRequest)
            const localVarPath = `/api/v1/mp/feedback`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'POST', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            localVarHeaderParameter['Content-Type'] = 'application/json';

            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };
            localVarRequestOptions.data = serializeDataIfNeeded(feedbackCreateRequest, localVarRequestOptions, configuration)

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 根据id查询意见反馈
         * @param {string} id 意见反馈id
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getFeedbackByIdAdmin: async (id: string, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'id' is not null or undefined
            assertParamExists('getFeedbackByIdAdmin', 'id', id)
            const localVarPath = `/api/v1/admin/feedback/{id}`
                .replace(`{${"id"}}`, encodeURIComponent(String(id)));
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 分页查询意见反馈
         * @param {number} [page] 页码，从1开始
         * @param {number} [size] 每页大小
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        pageFeedbackAdmin: async (page?: number, size?: number, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            const localVarPath = `/api/v1/admin/feedback/page`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)

            if (page !== undefined) {
                localVarQueryParameter['page'] = page;
            }

            if (size !== undefined) {
                localVarQueryParameter['size'] = size;
            }



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
    }
};

/**
 * DefaultApi - functional programming interface
 * @export
 */
export const DefaultApiFp = function (configuration?: Configuration) {
    const localVarAxiosParamCreator = DefaultApiAxiosParamCreator(configuration)
    return {
        /**
         * 
         * @summary 创建意见反馈
         * @param {FeedbackCreateRequest} feedbackCreateRequest 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async createFeedbackMp(feedbackCreateRequest: FeedbackCreateRequest, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<Feedback>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.createFeedbackMp(feedbackCreateRequest, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['DefaultApi.createFeedbackMp']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 根据id查询意见反馈
         * @param {string} id 意见反馈id
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async getFeedbackByIdAdmin(id: string, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<Feedback>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.getFeedbackByIdAdmin(id, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['DefaultApi.getFeedbackByIdAdmin']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 分页查询意见反馈
         * @param {number} [page] 页码，从1开始
         * @param {number} [size] 每页大小
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async pageFeedbackAdmin(page?: number, size?: number, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<PageFeedback>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.pageFeedbackAdmin(page, size, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['DefaultApi.pageFeedbackAdmin']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
    }
};

/**
 * DefaultApi - factory interface
 * @export
 */
export const DefaultApiFactory = function (configuration?: Configuration, basePath?: string, axios?: AxiosInstance) {
    const localVarFp = DefaultApiFp(configuration)
    return {
        /**
         * 
         * @summary 创建意见反馈
         * @param {DefaultApiCreateFeedbackMpRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        createFeedbackMp(requestParameters: DefaultApiCreateFeedbackMpRequest, options?: RawAxiosRequestConfig): AxiosPromise<Feedback> {
            return localVarFp.createFeedbackMp(requestParameters.feedbackCreateRequest, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 根据id查询意见反馈
         * @param {DefaultApiGetFeedbackByIdAdminRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getFeedbackByIdAdmin(requestParameters: DefaultApiGetFeedbackByIdAdminRequest, options?: RawAxiosRequestConfig): AxiosPromise<Feedback> {
            return localVarFp.getFeedbackByIdAdmin(requestParameters.id, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 分页查询意见反馈
         * @param {DefaultApiPageFeedbackAdminRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        pageFeedbackAdmin(requestParameters: DefaultApiPageFeedbackAdminRequest = {}, options?: RawAxiosRequestConfig): AxiosPromise<PageFeedback> {
            return localVarFp.pageFeedbackAdmin(requestParameters.page, requestParameters.size, options).then((request) => request(axios, basePath));
        },
    };
};

/**
 * Request parameters for createFeedbackMp operation in DefaultApi.
 * @export
 * @interface DefaultApiCreateFeedbackMpRequest
 */
export interface DefaultApiCreateFeedbackMpRequest {
    /**
     * 
     * @type {FeedbackCreateRequest}
     * @memberof DefaultApiCreateFeedbackMp
     */
    readonly feedbackCreateRequest: FeedbackCreateRequest
}

/**
 * Request parameters for getFeedbackByIdAdmin operation in DefaultApi.
 * @export
 * @interface DefaultApiGetFeedbackByIdAdminRequest
 */
export interface DefaultApiGetFeedbackByIdAdminRequest {
    /**
     * 意见反馈id
     * @type {string}
     * @memberof DefaultApiGetFeedbackByIdAdmin
     */
    readonly id: string
}

/**
 * Request parameters for pageFeedbackAdmin operation in DefaultApi.
 * @export
 * @interface DefaultApiPageFeedbackAdminRequest
 */
export interface DefaultApiPageFeedbackAdminRequest {
    /**
     * 页码，从1开始
     * @type {number}
     * @memberof DefaultApiPageFeedbackAdmin
     */
    readonly page?: number

    /**
     * 每页大小
     * @type {number}
     * @memberof DefaultApiPageFeedbackAdmin
     */
    readonly size?: number
}

/**
 * DefaultApi - object-oriented interface
 * @export
 * @class DefaultApi
 * @extends {BaseAPI}
 */
export class DefaultApi extends BaseAPI {
    /**
     * 
     * @summary 创建意见反馈
     * @param {DefaultApiCreateFeedbackMpRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof DefaultApi
     */
    public createFeedbackMp(requestParameters: DefaultApiCreateFeedbackMpRequest, options?: RawAxiosRequestConfig) {
        return DefaultApiFp(this.configuration).createFeedbackMp(requestParameters.feedbackCreateRequest, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 根据id查询意见反馈
     * @param {DefaultApiGetFeedbackByIdAdminRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof DefaultApi
     */
    public getFeedbackByIdAdmin(requestParameters: DefaultApiGetFeedbackByIdAdminRequest, options?: RawAxiosRequestConfig) {
        return DefaultApiFp(this.configuration).getFeedbackByIdAdmin(requestParameters.id, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 分页查询意见反馈
     * @param {DefaultApiPageFeedbackAdminRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof DefaultApi
     */
    public pageFeedbackAdmin(requestParameters: DefaultApiPageFeedbackAdminRequest = {}, options?: RawAxiosRequestConfig) {
        return DefaultApiFp(this.configuration).pageFeedbackAdmin(requestParameters.page, requestParameters.size, options).then((request) => request(this.axios, this.basePath));
    }
}



/**
 * ActivityAdminApi - axios parameter creator
 * @export
 */
export const ActivityAdminApiAxiosParamCreator = function (configuration?: Configuration) {
    return {
        /**
         * 
         * @summary 创建活动
         * @param {ActivitySaveRequest} activitySaveRequest 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        createActivity1: async (activitySaveRequest: ActivitySaveRequest, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'activitySaveRequest' is not null or undefined
            assertParamExists('createActivity1', 'activitySaveRequest', activitySaveRequest)
            const localVarPath = `/api/v1/admin/activity`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'POST', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            localVarHeaderParameter['Content-Type'] = 'application/json';

            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };
            localVarRequestOptions.data = serializeDataIfNeeded(activitySaveRequest, localVarRequestOptions, configuration)

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 根据id删除活动
         * @param {string} id 活动id
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        deleteActivityById: async (id: string, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'id' is not null or undefined
            assertParamExists('deleteActivityById', 'id', id)
            const localVarPath = `/api/v1/admin/activity/{id}`
                .replace(`{${"id"}}`, encodeURIComponent(String(id)));
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'DELETE', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 根据id查询活动
         * @param {string} id 活动id
         * @param {boolean} [needStatistics] 是否需要返回统计数据。默认为false
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getActivityById: async (id: string, needStatistics?: boolean, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'id' is not null or undefined
            assertParamExists('getActivityById', 'id', id)
            const localVarPath = `/api/v1/admin/activity/{id}`
                .replace(`{${"id"}}`, encodeURIComponent(String(id)));
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)

            if (needStatistics !== undefined) {
                localVarQueryParameter['needStatistics'] = needStatistics;
            }



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 查询所有活动列表
         * @param {boolean} [needStatistics] 是否需要返回统计数据。默认为false
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        listActivity: async (needStatistics?: boolean, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            const localVarPath = `/api/v1/admin/activity/list`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)

            if (needStatistics !== undefined) {
                localVarQueryParameter['needStatistics'] = needStatistics;
            }



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 更新活动
         * @param {string} id 活动id
         * @param {ActivitySaveRequest} activitySaveRequest 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        updateActivity1: async (id: string, activitySaveRequest: ActivitySaveRequest, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'id' is not null or undefined
            assertParamExists('updateActivity1', 'id', id)
            // verify required parameter 'activitySaveRequest' is not null or undefined
            assertParamExists('updateActivity1', 'activitySaveRequest', activitySaveRequest)
            const localVarPath = `/api/v1/admin/activity/{id}`
                .replace(`{${"id"}}`, encodeURIComponent(String(id)));
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'PUT', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            localVarHeaderParameter['Content-Type'] = 'application/json';

            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };
            localVarRequestOptions.data = serializeDataIfNeeded(activitySaveRequest, localVarRequestOptions, configuration)

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 更新活动发布状态
         * @param {string} id 活动id
         * @param {ActivityPublishUpdateRequest} activityPublishUpdateRequest 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        updateActivityPublish: async (id: string, activityPublishUpdateRequest: ActivityPublishUpdateRequest, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'id' is not null or undefined
            assertParamExists('updateActivityPublish', 'id', id)
            // verify required parameter 'activityPublishUpdateRequest' is not null or undefined
            assertParamExists('updateActivityPublish', 'activityPublishUpdateRequest', activityPublishUpdateRequest)
            const localVarPath = `/api/v1/admin/activity/{id}/publish`
                .replace(`{${"id"}}`, encodeURIComponent(String(id)));
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'PUT', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            localVarHeaderParameter['Content-Type'] = 'application/json';

            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };
            localVarRequestOptions.data = serializeDataIfNeeded(activityPublishUpdateRequest, localVarRequestOptions, configuration)

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
    }
};

/**
 * ActivityAdminApi - functional programming interface
 * @export
 */
export const ActivityAdminApiFp = function (configuration?: Configuration) {
    const localVarAxiosParamCreator = ActivityAdminApiAxiosParamCreator(configuration)
    return {
        /**
         * 
         * @summary 创建活动
         * @param {ActivitySaveRequest} activitySaveRequest 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async createActivity1(activitySaveRequest: ActivitySaveRequest, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<Activity>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.createActivity1(activitySaveRequest, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['ActivityAdminApi.createActivity1']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 根据id删除活动
         * @param {string} id 活动id
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async deleteActivityById(id: string, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<boolean>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.deleteActivityById(id, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['ActivityAdminApi.deleteActivityById']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 根据id查询活动
         * @param {string} id 活动id
         * @param {boolean} [needStatistics] 是否需要返回统计数据。默认为false
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async getActivityById(id: string, needStatistics?: boolean, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<Activity>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.getActivityById(id, needStatistics, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['ActivityAdminApi.getActivityById']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 查询所有活动列表
         * @param {boolean} [needStatistics] 是否需要返回统计数据。默认为false
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async listActivity(needStatistics?: boolean, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<Array<Activity>>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.listActivity(needStatistics, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['ActivityAdminApi.listActivity']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 更新活动
         * @param {string} id 活动id
         * @param {ActivitySaveRequest} activitySaveRequest 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async updateActivity1(id: string, activitySaveRequest: ActivitySaveRequest, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<boolean>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.updateActivity1(id, activitySaveRequest, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['ActivityAdminApi.updateActivity1']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 更新活动发布状态
         * @param {string} id 活动id
         * @param {ActivityPublishUpdateRequest} activityPublishUpdateRequest 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async updateActivityPublish(id: string, activityPublishUpdateRequest: ActivityPublishUpdateRequest, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<boolean>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.updateActivityPublish(id, activityPublishUpdateRequest, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['ActivityAdminApi.updateActivityPublish']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
    }
};

/**
 * ActivityAdminApi - factory interface
 * @export
 */
export const ActivityAdminApiFactory = function (configuration?: Configuration, basePath?: string, axios?: AxiosInstance) {
    const localVarFp = ActivityAdminApiFp(configuration)
    return {
        /**
         * 
         * @summary 创建活动
         * @param {ActivityAdminApiCreateActivity1Request} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        createActivity1(requestParameters: ActivityAdminApiCreateActivity1Request, options?: RawAxiosRequestConfig): AxiosPromise<Activity> {
            return localVarFp.createActivity1(requestParameters.activitySaveRequest, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 根据id删除活动
         * @param {ActivityAdminApiDeleteActivityByIdRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        deleteActivityById(requestParameters: ActivityAdminApiDeleteActivityByIdRequest, options?: RawAxiosRequestConfig): AxiosPromise<boolean> {
            return localVarFp.deleteActivityById(requestParameters.id, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 根据id查询活动
         * @param {ActivityAdminApiGetActivityByIdRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getActivityById(requestParameters: ActivityAdminApiGetActivityByIdRequest, options?: RawAxiosRequestConfig): AxiosPromise<Activity> {
            return localVarFp.getActivityById(requestParameters.id, requestParameters.needStatistics, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 查询所有活动列表
         * @param {ActivityAdminApiListActivityRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        listActivity(requestParameters: ActivityAdminApiListActivityRequest = {}, options?: RawAxiosRequestConfig): AxiosPromise<Array<Activity>> {
            return localVarFp.listActivity(requestParameters.needStatistics, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 更新活动
         * @param {ActivityAdminApiUpdateActivity1Request} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        updateActivity1(requestParameters: ActivityAdminApiUpdateActivity1Request, options?: RawAxiosRequestConfig): AxiosPromise<boolean> {
            return localVarFp.updateActivity1(requestParameters.id, requestParameters.activitySaveRequest, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 更新活动发布状态
         * @param {ActivityAdminApiUpdateActivityPublishRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        updateActivityPublish(requestParameters: ActivityAdminApiUpdateActivityPublishRequest, options?: RawAxiosRequestConfig): AxiosPromise<boolean> {
            return localVarFp.updateActivityPublish(requestParameters.id, requestParameters.activityPublishUpdateRequest, options).then((request) => request(axios, basePath));
        },
    };
};

/**
 * Request parameters for createActivity1 operation in ActivityAdminApi.
 * @export
 * @interface ActivityAdminApiCreateActivity1Request
 */
export interface ActivityAdminApiCreateActivity1Request {
    /**
     * 
     * @type {ActivitySaveRequest}
     * @memberof ActivityAdminApiCreateActivity1
     */
    readonly activitySaveRequest: ActivitySaveRequest
}

/**
 * Request parameters for deleteActivityById operation in ActivityAdminApi.
 * @export
 * @interface ActivityAdminApiDeleteActivityByIdRequest
 */
export interface ActivityAdminApiDeleteActivityByIdRequest {
    /**
     * 活动id
     * @type {string}
     * @memberof ActivityAdminApiDeleteActivityById
     */
    readonly id: string
}

/**
 * Request parameters for getActivityById operation in ActivityAdminApi.
 * @export
 * @interface ActivityAdminApiGetActivityByIdRequest
 */
export interface ActivityAdminApiGetActivityByIdRequest {
    /**
     * 活动id
     * @type {string}
     * @memberof ActivityAdminApiGetActivityById
     */
    readonly id: string

    /**
     * 是否需要返回统计数据。默认为false
     * @type {boolean}
     * @memberof ActivityAdminApiGetActivityById
     */
    readonly needStatistics?: boolean
}

/**
 * Request parameters for listActivity operation in ActivityAdminApi.
 * @export
 * @interface ActivityAdminApiListActivityRequest
 */
export interface ActivityAdminApiListActivityRequest {
    /**
     * 是否需要返回统计数据。默认为false
     * @type {boolean}
     * @memberof ActivityAdminApiListActivity
     */
    readonly needStatistics?: boolean
}

/**
 * Request parameters for updateActivity1 operation in ActivityAdminApi.
 * @export
 * @interface ActivityAdminApiUpdateActivity1Request
 */
export interface ActivityAdminApiUpdateActivity1Request {
    /**
     * 活动id
     * @type {string}
     * @memberof ActivityAdminApiUpdateActivity1
     */
    readonly id: string

    /**
     * 
     * @type {ActivitySaveRequest}
     * @memberof ActivityAdminApiUpdateActivity1
     */
    readonly activitySaveRequest: ActivitySaveRequest
}

/**
 * Request parameters for updateActivityPublish operation in ActivityAdminApi.
 * @export
 * @interface ActivityAdminApiUpdateActivityPublishRequest
 */
export interface ActivityAdminApiUpdateActivityPublishRequest {
    /**
     * 活动id
     * @type {string}
     * @memberof ActivityAdminApiUpdateActivityPublish
     */
    readonly id: string

    /**
     * 
     * @type {ActivityPublishUpdateRequest}
     * @memberof ActivityAdminApiUpdateActivityPublish
     */
    readonly activityPublishUpdateRequest: ActivityPublishUpdateRequest
}

/**
 * ActivityAdminApi - object-oriented interface
 * @export
 * @class ActivityAdminApi
 * @extends {BaseAPI}
 */
export class ActivityAdminApi extends BaseAPI {
    /**
     * 
     * @summary 创建活动
     * @param {ActivityAdminApiCreateActivity1Request} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof ActivityAdminApi
     */
    public createActivity1(requestParameters: ActivityAdminApiCreateActivity1Request, options?: RawAxiosRequestConfig) {
        return ActivityAdminApiFp(this.configuration).createActivity1(requestParameters.activitySaveRequest, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 根据id删除活动
     * @param {ActivityAdminApiDeleteActivityByIdRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof ActivityAdminApi
     */
    public deleteActivityById(requestParameters: ActivityAdminApiDeleteActivityByIdRequest, options?: RawAxiosRequestConfig) {
        return ActivityAdminApiFp(this.configuration).deleteActivityById(requestParameters.id, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 根据id查询活动
     * @param {ActivityAdminApiGetActivityByIdRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof ActivityAdminApi
     */
    public getActivityById(requestParameters: ActivityAdminApiGetActivityByIdRequest, options?: RawAxiosRequestConfig) {
        return ActivityAdminApiFp(this.configuration).getActivityById(requestParameters.id, requestParameters.needStatistics, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 查询所有活动列表
     * @param {ActivityAdminApiListActivityRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof ActivityAdminApi
     */
    public listActivity(requestParameters: ActivityAdminApiListActivityRequest = {}, options?: RawAxiosRequestConfig) {
        return ActivityAdminApiFp(this.configuration).listActivity(requestParameters.needStatistics, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 更新活动
     * @param {ActivityAdminApiUpdateActivity1Request} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof ActivityAdminApi
     */
    public updateActivity1(requestParameters: ActivityAdminApiUpdateActivity1Request, options?: RawAxiosRequestConfig) {
        return ActivityAdminApiFp(this.configuration).updateActivity1(requestParameters.id, requestParameters.activitySaveRequest, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 更新活动发布状态
     * @param {ActivityAdminApiUpdateActivityPublishRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof ActivityAdminApi
     */
    public updateActivityPublish(requestParameters: ActivityAdminApiUpdateActivityPublishRequest, options?: RawAxiosRequestConfig) {
        return ActivityAdminApiFp(this.configuration).updateActivityPublish(requestParameters.id, requestParameters.activityPublishUpdateRequest, options).then((request) => request(this.axios, this.basePath));
    }
}



/**
 * ActivityMpApi - axios parameter creator
 * @export
 */
export const ActivityMpApiAxiosParamCreator = function (configuration?: Configuration) {
    return {
        /**
         * 
         * @summary 查询累计签到奖励配置
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        listActivityMp: async (options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            const localVarPath = `/api/v1/mp/activity/list`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
    }
};

/**
 * ActivityMpApi - functional programming interface
 * @export
 */
export const ActivityMpApiFp = function (configuration?: Configuration) {
    const localVarAxiosParamCreator = ActivityMpApiAxiosParamCreator(configuration)
    return {
        /**
         * 
         * @summary 查询累计签到奖励配置
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async listActivityMp(options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<Array<Activity>>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.listActivityMp(options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['ActivityMpApi.listActivityMp']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
    }
};

/**
 * ActivityMpApi - factory interface
 * @export
 */
export const ActivityMpApiFactory = function (configuration?: Configuration, basePath?: string, axios?: AxiosInstance) {
    const localVarFp = ActivityMpApiFp(configuration)
    return {
        /**
         * 
         * @summary 查询累计签到奖励配置
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        listActivityMp(options?: RawAxiosRequestConfig): AxiosPromise<Array<Activity>> {
            return localVarFp.listActivityMp(options).then((request) => request(axios, basePath));
        },
    };
};

/**
 * ActivityMpApi - object-oriented interface
 * @export
 * @class ActivityMpApi
 * @extends {BaseAPI}
 */
export class ActivityMpApi extends BaseAPI {
    /**
     * 
     * @summary 查询累计签到奖励配置
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof ActivityMpApi
     */
    public listActivityMp(options?: RawAxiosRequestConfig) {
        return ActivityMpApiFp(this.configuration).listActivityMp(options).then((request) => request(this.axios, this.basePath));
    }
}



/**
 * AdminTokensApi - axios parameter creator
 * @export
 */
export const AdminTokensApiAxiosParamCreator = function (configuration?: Configuration) {
    return {
        /**
         * 
         * @summary 添加管理员
         * @param {CreateAdminRequest} createAdminRequest 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        addAdmin: async (createAdminRequest: CreateAdminRequest, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'createAdminRequest' is not null or undefined
            assertParamExists('addAdmin', 'createAdminRequest', createAdminRequest)
            const localVarPath = `/api/v1/admin/admins`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'POST', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            localVarHeaderParameter['Content-Type'] = 'application/json';

            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };
            localVarRequestOptions.data = serializeDataIfNeeded(createAdminRequest, localVarRequestOptions, configuration)

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 创建管理员访问凭据。
         * @param {string} user 
         * @param {string} password 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        createAdminToken: async (user: string, password: string, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'user' is not null or undefined
            assertParamExists('createAdminToken', 'user', user)
            // verify required parameter 'password' is not null or undefined
            assertParamExists('createAdminToken', 'password', password)
            const localVarPath = `/api/v1/admin/token`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'POST', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            if (user !== undefined) {
                localVarQueryParameter['user'] = user;
            }

            if (password !== undefined) {
                localVarQueryParameter['password'] = password;
            }



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 创建用户访问凭据。
         * @param {string} userId 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        createUserToken: async (userId: string, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'userId' is not null or undefined
            assertParamExists('createUserToken', 'userId', userId)
            const localVarPath = `/api/v1/admin/user-token`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'POST', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)

            if (userId !== undefined) {
                localVarQueryParameter['userId'] = userId;
            }



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 获取管理员列表
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getAdmins: async (options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            const localVarPath = `/api/v1/admin/admins`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 删除管理员
         * @param {string} email 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        removeAdmin: async (email: string, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'email' is not null or undefined
            assertParamExists('removeAdmin', 'email', email)
            const localVarPath = `/api/v1/admin/admins/{email}`
                .replace(`{${"email"}}`, encodeURIComponent(String(email)));
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'DELETE', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
    }
};

/**
 * AdminTokensApi - functional programming interface
 * @export
 */
export const AdminTokensApiFp = function (configuration?: Configuration) {
    const localVarAxiosParamCreator = AdminTokensApiAxiosParamCreator(configuration)
    return {
        /**
         * 
         * @summary 添加管理员
         * @param {CreateAdminRequest} createAdminRequest 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async addAdmin(createAdminRequest: CreateAdminRequest, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<AdminEntity>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.addAdmin(createAdminRequest, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['AdminTokensApi.addAdmin']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 创建管理员访问凭据。
         * @param {string} user 
         * @param {string} password 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async createAdminToken(user: string, password: string, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<string>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.createAdminToken(user, password, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['AdminTokensApi.createAdminToken']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 创建用户访问凭据。
         * @param {string} userId 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async createUserToken(userId: string, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<string>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.createUserToken(userId, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['AdminTokensApi.createUserToken']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 获取管理员列表
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async getAdmins(options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<Array<AdminEntity>>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.getAdmins(options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['AdminTokensApi.getAdmins']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 删除管理员
         * @param {string} email 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async removeAdmin(email: string, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<AdminEntity>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.removeAdmin(email, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['AdminTokensApi.removeAdmin']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
    }
};

/**
 * AdminTokensApi - factory interface
 * @export
 */
export const AdminTokensApiFactory = function (configuration?: Configuration, basePath?: string, axios?: AxiosInstance) {
    const localVarFp = AdminTokensApiFp(configuration)
    return {
        /**
         * 
         * @summary 添加管理员
         * @param {AdminTokensApiAddAdminRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        addAdmin(requestParameters: AdminTokensApiAddAdminRequest, options?: RawAxiosRequestConfig): AxiosPromise<AdminEntity> {
            return localVarFp.addAdmin(requestParameters.createAdminRequest, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 创建管理员访问凭据。
         * @param {AdminTokensApiCreateAdminTokenRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        createAdminToken(requestParameters: AdminTokensApiCreateAdminTokenRequest, options?: RawAxiosRequestConfig): AxiosPromise<string> {
            return localVarFp.createAdminToken(requestParameters.user, requestParameters.password, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 创建用户访问凭据。
         * @param {AdminTokensApiCreateUserTokenRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        createUserToken(requestParameters: AdminTokensApiCreateUserTokenRequest, options?: RawAxiosRequestConfig): AxiosPromise<string> {
            return localVarFp.createUserToken(requestParameters.userId, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 获取管理员列表
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getAdmins(options?: RawAxiosRequestConfig): AxiosPromise<Array<AdminEntity>> {
            return localVarFp.getAdmins(options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 删除管理员
         * @param {AdminTokensApiRemoveAdminRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        removeAdmin(requestParameters: AdminTokensApiRemoveAdminRequest, options?: RawAxiosRequestConfig): AxiosPromise<AdminEntity> {
            return localVarFp.removeAdmin(requestParameters.email, options).then((request) => request(axios, basePath));
        },
    };
};

/**
 * Request parameters for addAdmin operation in AdminTokensApi.
 * @export
 * @interface AdminTokensApiAddAdminRequest
 */
export interface AdminTokensApiAddAdminRequest {
    /**
     * 
     * @type {CreateAdminRequest}
     * @memberof AdminTokensApiAddAdmin
     */
    readonly createAdminRequest: CreateAdminRequest
}

/**
 * Request parameters for createAdminToken operation in AdminTokensApi.
 * @export
 * @interface AdminTokensApiCreateAdminTokenRequest
 */
export interface AdminTokensApiCreateAdminTokenRequest {
    /**
     * 
     * @type {string}
     * @memberof AdminTokensApiCreateAdminToken
     */
    readonly user: string

    /**
     * 
     * @type {string}
     * @memberof AdminTokensApiCreateAdminToken
     */
    readonly password: string
}

/**
 * Request parameters for createUserToken operation in AdminTokensApi.
 * @export
 * @interface AdminTokensApiCreateUserTokenRequest
 */
export interface AdminTokensApiCreateUserTokenRequest {
    /**
     * 
     * @type {string}
     * @memberof AdminTokensApiCreateUserToken
     */
    readonly userId: string
}

/**
 * Request parameters for removeAdmin operation in AdminTokensApi.
 * @export
 * @interface AdminTokensApiRemoveAdminRequest
 */
export interface AdminTokensApiRemoveAdminRequest {
    /**
     * 
     * @type {string}
     * @memberof AdminTokensApiRemoveAdmin
     */
    readonly email: string
}

/**
 * AdminTokensApi - object-oriented interface
 * @export
 * @class AdminTokensApi
 * @extends {BaseAPI}
 */
export class AdminTokensApi extends BaseAPI {
    /**
     * 
     * @summary 添加管理员
     * @param {AdminTokensApiAddAdminRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof AdminTokensApi
     */
    public addAdmin(requestParameters: AdminTokensApiAddAdminRequest, options?: RawAxiosRequestConfig) {
        return AdminTokensApiFp(this.configuration).addAdmin(requestParameters.createAdminRequest, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 创建管理员访问凭据。
     * @param {AdminTokensApiCreateAdminTokenRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof AdminTokensApi
     */
    public createAdminToken(requestParameters: AdminTokensApiCreateAdminTokenRequest, options?: RawAxiosRequestConfig) {
        return AdminTokensApiFp(this.configuration).createAdminToken(requestParameters.user, requestParameters.password, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 创建用户访问凭据。
     * @param {AdminTokensApiCreateUserTokenRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof AdminTokensApi
     */
    public createUserToken(requestParameters: AdminTokensApiCreateUserTokenRequest, options?: RawAxiosRequestConfig) {
        return AdminTokensApiFp(this.configuration).createUserToken(requestParameters.userId, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 获取管理员列表
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof AdminTokensApi
     */
    public getAdmins(options?: RawAxiosRequestConfig) {
        return AdminTokensApiFp(this.configuration).getAdmins(options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 删除管理员
     * @param {AdminTokensApiRemoveAdminRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof AdminTokensApi
     */
    public removeAdmin(requestParameters: AdminTokensApiRemoveAdminRequest, options?: RawAxiosRequestConfig) {
        return AdminTokensApiFp(this.configuration).removeAdmin(requestParameters.email, options).then((request) => request(this.axios, this.basePath));
    }
}



/**
 * BlockerApi - axios parameter creator
 * @export
 */
export const BlockerApiAxiosParamCreator = function (configuration?: Configuration) {
    return {
        /**
         * \'PREPARE\'表示活动未开始，\'PENDING\'表示活动进行中，\'FINISHED\'表示活动已结束，\'UNKNOWN\'表示未知状态, 未知状态请和后端确认。
         * @summary 依据当前时间获取后端的block状态
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getStatuses: async (options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            const localVarPath = `/api/v1/blocker/status`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
    }
};

/**
 * BlockerApi - functional programming interface
 * @export
 */
export const BlockerApiFp = function (configuration?: Configuration) {
    const localVarAxiosParamCreator = BlockerApiAxiosParamCreator(configuration)
    return {
        /**
         * \'PREPARE\'表示活动未开始，\'PENDING\'表示活动进行中，\'FINISHED\'表示活动已结束，\'UNKNOWN\'表示未知状态, 未知状态请和后端确认。
         * @summary 依据当前时间获取后端的block状态
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async getStatuses(options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<BlockStatusResp>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.getStatuses(options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['BlockerApi.getStatuses']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
    }
};

/**
 * BlockerApi - factory interface
 * @export
 */
export const BlockerApiFactory = function (configuration?: Configuration, basePath?: string, axios?: AxiosInstance) {
    const localVarFp = BlockerApiFp(configuration)
    return {
        /**
         * \'PREPARE\'表示活动未开始，\'PENDING\'表示活动进行中，\'FINISHED\'表示活动已结束，\'UNKNOWN\'表示未知状态, 未知状态请和后端确认。
         * @summary 依据当前时间获取后端的block状态
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getStatuses(options?: RawAxiosRequestConfig): AxiosPromise<BlockStatusResp> {
            return localVarFp.getStatuses(options).then((request) => request(axios, basePath));
        },
    };
};

/**
 * BlockerApi - object-oriented interface
 * @export
 * @class BlockerApi
 * @extends {BaseAPI}
 */
export class BlockerApi extends BaseAPI {
    /**
     * \'PREPARE\'表示活动未开始，\'PENDING\'表示活动进行中，\'FINISHED\'表示活动已结束，\'UNKNOWN\'表示未知状态, 未知状态请和后端确认。
     * @summary 依据当前时间获取后端的block状态
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof BlockerApi
     */
    public getStatuses(options?: RawAxiosRequestConfig) {
        return BlockerApiFp(this.configuration).getStatuses(options).then((request) => request(this.axios, this.basePath));
    }
}



/**
 * CumulativeSignInConfigAdminApi - axios parameter creator
 * @export
 */
export const CumulativeSignInConfigAdminApiAxiosParamCreator = function (configuration?: Configuration) {
    return {
        /**
         * 
         * @summary 查询累计签到奖励配置
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getCumulativeSignInConfigAdmin: async (options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            const localVarPath = `/api/v1/admin/cumulative-sign-in-config`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 保存累计签到奖励配置
         * @param {CumulativeSignInConfigSaveRequest} cumulativeSignInConfigSaveRequest 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        saveCumulativeSignInConfigAdmin: async (cumulativeSignInConfigSaveRequest: CumulativeSignInConfigSaveRequest, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'cumulativeSignInConfigSaveRequest' is not null or undefined
            assertParamExists('saveCumulativeSignInConfigAdmin', 'cumulativeSignInConfigSaveRequest', cumulativeSignInConfigSaveRequest)
            const localVarPath = `/api/v1/admin/cumulative-sign-in-config`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'POST', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            localVarHeaderParameter['Content-Type'] = 'application/json';

            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };
            localVarRequestOptions.data = serializeDataIfNeeded(cumulativeSignInConfigSaveRequest, localVarRequestOptions, configuration)

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
    }
};

/**
 * CumulativeSignInConfigAdminApi - functional programming interface
 * @export
 */
export const CumulativeSignInConfigAdminApiFp = function (configuration?: Configuration) {
    const localVarAxiosParamCreator = CumulativeSignInConfigAdminApiAxiosParamCreator(configuration)
    return {
        /**
         * 
         * @summary 查询累计签到奖励配置
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async getCumulativeSignInConfigAdmin(options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<CumulativeSignInConfig>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.getCumulativeSignInConfigAdmin(options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['CumulativeSignInConfigAdminApi.getCumulativeSignInConfigAdmin']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 保存累计签到奖励配置
         * @param {CumulativeSignInConfigSaveRequest} cumulativeSignInConfigSaveRequest 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async saveCumulativeSignInConfigAdmin(cumulativeSignInConfigSaveRequest: CumulativeSignInConfigSaveRequest, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<CumulativeSignInConfig>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.saveCumulativeSignInConfigAdmin(cumulativeSignInConfigSaveRequest, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['CumulativeSignInConfigAdminApi.saveCumulativeSignInConfigAdmin']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
    }
};

/**
 * CumulativeSignInConfigAdminApi - factory interface
 * @export
 */
export const CumulativeSignInConfigAdminApiFactory = function (configuration?: Configuration, basePath?: string, axios?: AxiosInstance) {
    const localVarFp = CumulativeSignInConfigAdminApiFp(configuration)
    return {
        /**
         * 
         * @summary 查询累计签到奖励配置
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getCumulativeSignInConfigAdmin(options?: RawAxiosRequestConfig): AxiosPromise<CumulativeSignInConfig> {
            return localVarFp.getCumulativeSignInConfigAdmin(options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 保存累计签到奖励配置
         * @param {CumulativeSignInConfigAdminApiSaveCumulativeSignInConfigAdminRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        saveCumulativeSignInConfigAdmin(requestParameters: CumulativeSignInConfigAdminApiSaveCumulativeSignInConfigAdminRequest, options?: RawAxiosRequestConfig): AxiosPromise<CumulativeSignInConfig> {
            return localVarFp.saveCumulativeSignInConfigAdmin(requestParameters.cumulativeSignInConfigSaveRequest, options).then((request) => request(axios, basePath));
        },
    };
};

/**
 * Request parameters for saveCumulativeSignInConfigAdmin operation in CumulativeSignInConfigAdminApi.
 * @export
 * @interface CumulativeSignInConfigAdminApiSaveCumulativeSignInConfigAdminRequest
 */
export interface CumulativeSignInConfigAdminApiSaveCumulativeSignInConfigAdminRequest {
    /**
     * 
     * @type {CumulativeSignInConfigSaveRequest}
     * @memberof CumulativeSignInConfigAdminApiSaveCumulativeSignInConfigAdmin
     */
    readonly cumulativeSignInConfigSaveRequest: CumulativeSignInConfigSaveRequest
}

/**
 * CumulativeSignInConfigAdminApi - object-oriented interface
 * @export
 * @class CumulativeSignInConfigAdminApi
 * @extends {BaseAPI}
 */
export class CumulativeSignInConfigAdminApi extends BaseAPI {
    /**
     * 
     * @summary 查询累计签到奖励配置
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof CumulativeSignInConfigAdminApi
     */
    public getCumulativeSignInConfigAdmin(options?: RawAxiosRequestConfig) {
        return CumulativeSignInConfigAdminApiFp(this.configuration).getCumulativeSignInConfigAdmin(options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 保存累计签到奖励配置
     * @param {CumulativeSignInConfigAdminApiSaveCumulativeSignInConfigAdminRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof CumulativeSignInConfigAdminApi
     */
    public saveCumulativeSignInConfigAdmin(requestParameters: CumulativeSignInConfigAdminApiSaveCumulativeSignInConfigAdminRequest, options?: RawAxiosRequestConfig) {
        return CumulativeSignInConfigAdminApiFp(this.configuration).saveCumulativeSignInConfigAdmin(requestParameters.cumulativeSignInConfigSaveRequest, options).then((request) => request(this.axios, this.basePath));
    }
}



/**
 * CumulativeSignInConfigMpApi - axios parameter creator
 * @export
 */
export const CumulativeSignInConfigMpApiAxiosParamCreator = function (configuration?: Configuration) {
    return {
        /**
         * 
         * @summary 查询累计签到奖励配置
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getCumulativeSignInConfigMp: async (options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            const localVarPath = `/api/v1/mp/cumulative-sign-in-config`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 查询最近一条签到记录
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getLastCumulativeSignInRecordMp: async (options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            const localVarPath = `/api/v1/mp/cumulative-sign-in-config/last`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 签到
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        signInMp: async (options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            const localVarPath = `/api/v1/mp/cumulative-sign-in-config`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'POST', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
    }
};

/**
 * CumulativeSignInConfigMpApi - functional programming interface
 * @export
 */
export const CumulativeSignInConfigMpApiFp = function (configuration?: Configuration) {
    const localVarAxiosParamCreator = CumulativeSignInConfigMpApiAxiosParamCreator(configuration)
    return {
        /**
         * 
         * @summary 查询累计签到奖励配置
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async getCumulativeSignInConfigMp(options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<CumulativeSignInConfig>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.getCumulativeSignInConfigMp(options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['CumulativeSignInConfigMpApi.getCumulativeSignInConfigMp']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 查询最近一条签到记录
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async getLastCumulativeSignInRecordMp(options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<CumulativeSignInRecord>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.getLastCumulativeSignInRecordMp(options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['CumulativeSignInConfigMpApi.getLastCumulativeSignInRecordMp']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 签到
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async signInMp(options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<CumulativeSignInRecord>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.signInMp(options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['CumulativeSignInConfigMpApi.signInMp']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
    }
};

/**
 * CumulativeSignInConfigMpApi - factory interface
 * @export
 */
export const CumulativeSignInConfigMpApiFactory = function (configuration?: Configuration, basePath?: string, axios?: AxiosInstance) {
    const localVarFp = CumulativeSignInConfigMpApiFp(configuration)
    return {
        /**
         * 
         * @summary 查询累计签到奖励配置
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getCumulativeSignInConfigMp(options?: RawAxiosRequestConfig): AxiosPromise<CumulativeSignInConfig> {
            return localVarFp.getCumulativeSignInConfigMp(options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 查询最近一条签到记录
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getLastCumulativeSignInRecordMp(options?: RawAxiosRequestConfig): AxiosPromise<CumulativeSignInRecord> {
            return localVarFp.getLastCumulativeSignInRecordMp(options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 签到
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        signInMp(options?: RawAxiosRequestConfig): AxiosPromise<CumulativeSignInRecord> {
            return localVarFp.signInMp(options).then((request) => request(axios, basePath));
        },
    };
};

/**
 * CumulativeSignInConfigMpApi - object-oriented interface
 * @export
 * @class CumulativeSignInConfigMpApi
 * @extends {BaseAPI}
 */
export class CumulativeSignInConfigMpApi extends BaseAPI {
    /**
     * 
     * @summary 查询累计签到奖励配置
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof CumulativeSignInConfigMpApi
     */
    public getCumulativeSignInConfigMp(options?: RawAxiosRequestConfig) {
        return CumulativeSignInConfigMpApiFp(this.configuration).getCumulativeSignInConfigMp(options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 查询最近一条签到记录
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof CumulativeSignInConfigMpApi
     */
    public getLastCumulativeSignInRecordMp(options?: RawAxiosRequestConfig) {
        return CumulativeSignInConfigMpApiFp(this.configuration).getLastCumulativeSignInRecordMp(options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 签到
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof CumulativeSignInConfigMpApi
     */
    public signInMp(options?: RawAxiosRequestConfig) {
        return CumulativeSignInConfigMpApiFp(this.configuration).signInMp(options).then((request) => request(this.axios, this.basePath));
    }
}



/**
 * CumulativeSignInNotifyTaskMpApi - axios parameter creator
 * @export
 */
export const CumulativeSignInNotifyTaskMpApiAxiosParamCreator = function (configuration?: Configuration) {
    return {
        /**
         * 
         * @summary 查询当前用户今天是否已经订阅了明天的消息
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        checkCumulativeSignInNotifyTaskMp: async (options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            const localVarPath = `/api/v1/mp/cumulative-sign-in-notify-task/check`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 创建明天的累计签到通知任务
         * @param {NotifyTaskCreateRequest} notifyTaskCreateRequest 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        createCumulativeSignInNotifyTaskMp: async (notifyTaskCreateRequest: NotifyTaskCreateRequest, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'notifyTaskCreateRequest' is not null or undefined
            assertParamExists('createCumulativeSignInNotifyTaskMp', 'notifyTaskCreateRequest', notifyTaskCreateRequest)
            const localVarPath = `/api/v1/mp/cumulative-sign-in-notify-task`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'POST', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            localVarHeaderParameter['Content-Type'] = 'application/json';

            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };
            localVarRequestOptions.data = serializeDataIfNeeded(notifyTaskCreateRequest, localVarRequestOptions, configuration)

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
    }
};

/**
 * CumulativeSignInNotifyTaskMpApi - functional programming interface
 * @export
 */
export const CumulativeSignInNotifyTaskMpApiFp = function (configuration?: Configuration) {
    const localVarAxiosParamCreator = CumulativeSignInNotifyTaskMpApiAxiosParamCreator(configuration)
    return {
        /**
         * 
         * @summary 查询当前用户今天是否已经订阅了明天的消息
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async checkCumulativeSignInNotifyTaskMp(options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<boolean>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.checkCumulativeSignInNotifyTaskMp(options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['CumulativeSignInNotifyTaskMpApi.checkCumulativeSignInNotifyTaskMp']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 创建明天的累计签到通知任务
         * @param {NotifyTaskCreateRequest} notifyTaskCreateRequest 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async createCumulativeSignInNotifyTaskMp(notifyTaskCreateRequest: NotifyTaskCreateRequest, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<NotifyTask>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.createCumulativeSignInNotifyTaskMp(notifyTaskCreateRequest, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['CumulativeSignInNotifyTaskMpApi.createCumulativeSignInNotifyTaskMp']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
    }
};

/**
 * CumulativeSignInNotifyTaskMpApi - factory interface
 * @export
 */
export const CumulativeSignInNotifyTaskMpApiFactory = function (configuration?: Configuration, basePath?: string, axios?: AxiosInstance) {
    const localVarFp = CumulativeSignInNotifyTaskMpApiFp(configuration)
    return {
        /**
         * 
         * @summary 查询当前用户今天是否已经订阅了明天的消息
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        checkCumulativeSignInNotifyTaskMp(options?: RawAxiosRequestConfig): AxiosPromise<boolean> {
            return localVarFp.checkCumulativeSignInNotifyTaskMp(options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 创建明天的累计签到通知任务
         * @param {CumulativeSignInNotifyTaskMpApiCreateCumulativeSignInNotifyTaskMpRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        createCumulativeSignInNotifyTaskMp(requestParameters: CumulativeSignInNotifyTaskMpApiCreateCumulativeSignInNotifyTaskMpRequest, options?: RawAxiosRequestConfig): AxiosPromise<NotifyTask> {
            return localVarFp.createCumulativeSignInNotifyTaskMp(requestParameters.notifyTaskCreateRequest, options).then((request) => request(axios, basePath));
        },
    };
};

/**
 * Request parameters for createCumulativeSignInNotifyTaskMp operation in CumulativeSignInNotifyTaskMpApi.
 * @export
 * @interface CumulativeSignInNotifyTaskMpApiCreateCumulativeSignInNotifyTaskMpRequest
 */
export interface CumulativeSignInNotifyTaskMpApiCreateCumulativeSignInNotifyTaskMpRequest {
    /**
     * 
     * @type {NotifyTaskCreateRequest}
     * @memberof CumulativeSignInNotifyTaskMpApiCreateCumulativeSignInNotifyTaskMp
     */
    readonly notifyTaskCreateRequest: NotifyTaskCreateRequest
}

/**
 * CumulativeSignInNotifyTaskMpApi - object-oriented interface
 * @export
 * @class CumulativeSignInNotifyTaskMpApi
 * @extends {BaseAPI}
 */
export class CumulativeSignInNotifyTaskMpApi extends BaseAPI {
    /**
     * 
     * @summary 查询当前用户今天是否已经订阅了明天的消息
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof CumulativeSignInNotifyTaskMpApi
     */
    public checkCumulativeSignInNotifyTaskMp(options?: RawAxiosRequestConfig) {
        return CumulativeSignInNotifyTaskMpApiFp(this.configuration).checkCumulativeSignInNotifyTaskMp(options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 创建明天的累计签到通知任务
     * @param {CumulativeSignInNotifyTaskMpApiCreateCumulativeSignInNotifyTaskMpRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof CumulativeSignInNotifyTaskMpApi
     */
    public createCumulativeSignInNotifyTaskMp(requestParameters: CumulativeSignInNotifyTaskMpApiCreateCumulativeSignInNotifyTaskMpRequest, options?: RawAxiosRequestConfig) {
        return CumulativeSignInNotifyTaskMpApiFp(this.configuration).createCumulativeSignInNotifyTaskMp(requestParameters.notifyTaskCreateRequest, options).then((request) => request(this.axios, this.basePath));
    }
}



/**
 * DahuaAuthTokenApi - axios parameter creator
 * @export
 */
export const DahuaAuthTokenApiAxiosParamCreator = function (configuration?: Configuration) {
    return {
        /**
         * 
         * @summary 通过 免登 Token 获取登录凭据
         * @param {string} authToken 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getTokenByAuthToken: async (authToken: string, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'authToken' is not null or undefined
            assertParamExists('getTokenByAuthToken', 'authToken', authToken)
            const localVarPath = `/api/v1/ntes-dahua/token`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'POST', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)

            if (authToken !== undefined) {
                localVarQueryParameter['authToken'] = authToken;
            }



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
    }
};

/**
 * DahuaAuthTokenApi - functional programming interface
 * @export
 */
export const DahuaAuthTokenApiFp = function (configuration?: Configuration) {
    const localVarAxiosParamCreator = DahuaAuthTokenApiAxiosParamCreator(configuration)
    return {
        /**
         * 
         * @summary 通过 免登 Token 获取登录凭据
         * @param {string} authToken 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async getTokenByAuthToken(authToken: string, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<string>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.getTokenByAuthToken(authToken, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['DahuaAuthTokenApi.getTokenByAuthToken']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
    }
};

/**
 * DahuaAuthTokenApi - factory interface
 * @export
 */
export const DahuaAuthTokenApiFactory = function (configuration?: Configuration, basePath?: string, axios?: AxiosInstance) {
    const localVarFp = DahuaAuthTokenApiFp(configuration)
    return {
        /**
         * 
         * @summary 通过 免登 Token 获取登录凭据
         * @param {DahuaAuthTokenApiGetTokenByAuthTokenRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getTokenByAuthToken(requestParameters: DahuaAuthTokenApiGetTokenByAuthTokenRequest, options?: RawAxiosRequestConfig): AxiosPromise<string> {
            return localVarFp.getTokenByAuthToken(requestParameters.authToken, options).then((request) => request(axios, basePath));
        },
    };
};

/**
 * Request parameters for getTokenByAuthToken operation in DahuaAuthTokenApi.
 * @export
 * @interface DahuaAuthTokenApiGetTokenByAuthTokenRequest
 */
export interface DahuaAuthTokenApiGetTokenByAuthTokenRequest {
    /**
     * 
     * @type {string}
     * @memberof DahuaAuthTokenApiGetTokenByAuthToken
     */
    readonly authToken: string
}

/**
 * DahuaAuthTokenApi - object-oriented interface
 * @export
 * @class DahuaAuthTokenApi
 * @extends {BaseAPI}
 */
export class DahuaAuthTokenApi extends BaseAPI {
    /**
     * 
     * @summary 通过 免登 Token 获取登录凭据
     * @param {DahuaAuthTokenApiGetTokenByAuthTokenRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof DahuaAuthTokenApi
     */
    public getTokenByAuthToken(requestParameters: DahuaAuthTokenApiGetTokenByAuthTokenRequest, options?: RawAxiosRequestConfig) {
        return DahuaAuthTokenApiFp(this.configuration).getTokenByAuthToken(requestParameters.authToken, options).then((request) => request(this.axios, this.basePath));
    }
}



/**
 * DataCollectorApi - axios parameter creator
 * @export
 */
export const DataCollectorApiAxiosParamCreator = function (configuration?: Configuration) {
    return {
        /**
         * 
         * @summary 获取数据收集信息
         * @param {Array<string>} [name] 
         * @param {string} [start] 
         * @param {string} [end] 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getDataInfos: async (name?: Array<string>, start?: string, end?: string, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            const localVarPath = `/api/v1/data-collector/data-infos`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)

            if (name) {
                localVarQueryParameter['name'] = name;
            }

            if (start !== undefined) {
                localVarQueryParameter['start'] = (start as any instanceof Date) ?
                    (start as any).toISOString() :
                    start;
            }

            if (end !== undefined) {
                localVarQueryParameter['end'] = (end as any instanceof Date) ?
                    (end as any).toISOString() :
                    end;
            }



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 获取数据收集信息 Excel
         * @param {Array<string>} [name] 
         * @param {string} [start] 
         * @param {string} [end] 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getDataInfosExcel: async (name?: Array<string>, start?: string, end?: string, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            const localVarPath = `/api/v1/data-collector/data-infos-excel`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)

            if (name) {
                localVarQueryParameter['name'] = name;
            }

            if (start !== undefined) {
                localVarQueryParameter['start'] = (start as any instanceof Date) ?
                    (start as any).toISOString() :
                    start;
            }

            if (end !== undefined) {
                localVarQueryParameter['end'] = (end as any instanceof Date) ?
                    (end as any).toISOString() :
                    end;
            }



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
    }
};

/**
 * DataCollectorApi - functional programming interface
 * @export
 */
export const DataCollectorApiFp = function (configuration?: Configuration) {
    const localVarAxiosParamCreator = DataCollectorApiAxiosParamCreator(configuration)
    return {
        /**
         * 
         * @summary 获取数据收集信息
         * @param {Array<string>} [name] 
         * @param {string} [start] 
         * @param {string} [end] 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async getDataInfos(name?: Array<string>, start?: string, end?: string, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<{ [key: string]: { [key: string]: { [key: string]: number; }; }; }>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.getDataInfos(name, start, end, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['DataCollectorApi.getDataInfos']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 获取数据收集信息 Excel
         * @param {Array<string>} [name] 
         * @param {string} [start] 
         * @param {string} [end] 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async getDataInfosExcel(name?: Array<string>, start?: string, end?: string, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<Array<string>>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.getDataInfosExcel(name, start, end, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['DataCollectorApi.getDataInfosExcel']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
    }
};

/**
 * DataCollectorApi - factory interface
 * @export
 */
export const DataCollectorApiFactory = function (configuration?: Configuration, basePath?: string, axios?: AxiosInstance) {
    const localVarFp = DataCollectorApiFp(configuration)
    return {
        /**
         * 
         * @summary 获取数据收集信息
         * @param {DataCollectorApiGetDataInfosRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getDataInfos(requestParameters: DataCollectorApiGetDataInfosRequest = {}, options?: RawAxiosRequestConfig): AxiosPromise<{ [key: string]: { [key: string]: { [key: string]: number; }; }; }> {
            return localVarFp.getDataInfos(requestParameters.name, requestParameters.start, requestParameters.end, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 获取数据收集信息 Excel
         * @param {DataCollectorApiGetDataInfosExcelRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getDataInfosExcel(requestParameters: DataCollectorApiGetDataInfosExcelRequest = {}, options?: RawAxiosRequestConfig): AxiosPromise<Array<string>> {
            return localVarFp.getDataInfosExcel(requestParameters.name, requestParameters.start, requestParameters.end, options).then((request) => request(axios, basePath));
        },
    };
};

/**
 * Request parameters for getDataInfos operation in DataCollectorApi.
 * @export
 * @interface DataCollectorApiGetDataInfosRequest
 */
export interface DataCollectorApiGetDataInfosRequest {
    /**
     * 
     * @type {Array<string>}
     * @memberof DataCollectorApiGetDataInfos
     */
    readonly name?: Array<string>

    /**
     * 
     * @type {string}
     * @memberof DataCollectorApiGetDataInfos
     */
    readonly start?: string

    /**
     * 
     * @type {string}
     * @memberof DataCollectorApiGetDataInfos
     */
    readonly end?: string
}

/**
 * Request parameters for getDataInfosExcel operation in DataCollectorApi.
 * @export
 * @interface DataCollectorApiGetDataInfosExcelRequest
 */
export interface DataCollectorApiGetDataInfosExcelRequest {
    /**
     * 
     * @type {Array<string>}
     * @memberof DataCollectorApiGetDataInfosExcel
     */
    readonly name?: Array<string>

    /**
     * 
     * @type {string}
     * @memberof DataCollectorApiGetDataInfosExcel
     */
    readonly start?: string

    /**
     * 
     * @type {string}
     * @memberof DataCollectorApiGetDataInfosExcel
     */
    readonly end?: string
}

/**
 * DataCollectorApi - object-oriented interface
 * @export
 * @class DataCollectorApi
 * @extends {BaseAPI}
 */
export class DataCollectorApi extends BaseAPI {
    /**
     * 
     * @summary 获取数据收集信息
     * @param {DataCollectorApiGetDataInfosRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof DataCollectorApi
     */
    public getDataInfos(requestParameters: DataCollectorApiGetDataInfosRequest = {}, options?: RawAxiosRequestConfig) {
        return DataCollectorApiFp(this.configuration).getDataInfos(requestParameters.name, requestParameters.start, requestParameters.end, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 获取数据收集信息 Excel
     * @param {DataCollectorApiGetDataInfosExcelRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof DataCollectorApi
     */
    public getDataInfosExcel(requestParameters: DataCollectorApiGetDataInfosExcelRequest = {}, options?: RawAxiosRequestConfig) {
        return DataCollectorApiFp(this.configuration).getDataInfosExcel(requestParameters.name, requestParameters.start, requestParameters.end, options).then((request) => request(this.axios, this.basePath));
    }
}



/**
 * DictApi - axios parameter creator
 * @export
 */
export const DictApiAxiosParamCreator = function (configuration?: Configuration) {
    return {
        /**
         * 
         * @summary 创建字典项
         * @param {DictSaveRequest} dictSaveRequest 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        createDict: async (dictSaveRequest: DictSaveRequest, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'dictSaveRequest' is not null or undefined
            assertParamExists('createDict', 'dictSaveRequest', dictSaveRequest)
            const localVarPath = `/api/v1/dict`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'POST', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            localVarHeaderParameter['Content-Type'] = 'application/json';

            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };
            localVarRequestOptions.data = serializeDataIfNeeded(dictSaveRequest, localVarRequestOptions, configuration)

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 根据key或者字典项查询对应的值
         * @param {string} key 字典key
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getDictByKey: async (key: string, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'key' is not null or undefined
            assertParamExists('getDictByKey', 'key', key)
            const localVarPath = `/api/v1/dict/{key}`
                .replace(`{${"key"}}`, encodeURIComponent(String(key)));
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 列出所有字典项目
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        listDict: async (options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            const localVarPath = `/api/v1/dict/list`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 更新字典项
         * @param {string} key 
         * @param {DictSaveRequest} dictSaveRequest 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        updateDict: async (key: string, dictSaveRequest: DictSaveRequest, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'key' is not null or undefined
            assertParamExists('updateDict', 'key', key)
            // verify required parameter 'dictSaveRequest' is not null or undefined
            assertParamExists('updateDict', 'dictSaveRequest', dictSaveRequest)
            const localVarPath = `/api/v1/dict/{key}`
                .replace(`{${"key"}}`, encodeURIComponent(String(key)));
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'PUT', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            localVarHeaderParameter['Content-Type'] = 'application/json';

            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };
            localVarRequestOptions.data = serializeDataIfNeeded(dictSaveRequest, localVarRequestOptions, configuration)

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 删除字典项
         * @param {string} key 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        updateDict1: async (key: string, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'key' is not null or undefined
            assertParamExists('updateDict1', 'key', key)
            const localVarPath = `/api/v1/dict/{key}`
                .replace(`{${"key"}}`, encodeURIComponent(String(key)));
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'DELETE', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
    }
};

/**
 * DictApi - functional programming interface
 * @export
 */
export const DictApiFp = function (configuration?: Configuration) {
    const localVarAxiosParamCreator = DictApiAxiosParamCreator(configuration)
    return {
        /**
         * 
         * @summary 创建字典项
         * @param {DictSaveRequest} dictSaveRequest 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async createDict(dictSaveRequest: DictSaveRequest, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<Dict>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.createDict(dictSaveRequest, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['DictApi.createDict']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 根据key或者字典项查询对应的值
         * @param {string} key 字典key
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async getDictByKey(key: string, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<Dict>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.getDictByKey(key, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['DictApi.getDictByKey']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 列出所有字典项目
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async listDict(options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<Array<Dict>>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.listDict(options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['DictApi.listDict']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 更新字典项
         * @param {string} key 
         * @param {DictSaveRequest} dictSaveRequest 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async updateDict(key: string, dictSaveRequest: DictSaveRequest, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<Dict>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.updateDict(key, dictSaveRequest, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['DictApi.updateDict']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 删除字典项
         * @param {string} key 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async updateDict1(key: string, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<boolean>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.updateDict1(key, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['DictApi.updateDict1']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
    }
};

/**
 * DictApi - factory interface
 * @export
 */
export const DictApiFactory = function (configuration?: Configuration, basePath?: string, axios?: AxiosInstance) {
    const localVarFp = DictApiFp(configuration)
    return {
        /**
         * 
         * @summary 创建字典项
         * @param {DictApiCreateDictRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        createDict(requestParameters: DictApiCreateDictRequest, options?: RawAxiosRequestConfig): AxiosPromise<Dict> {
            return localVarFp.createDict(requestParameters.dictSaveRequest, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 根据key或者字典项查询对应的值
         * @param {DictApiGetDictByKeyRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getDictByKey(requestParameters: DictApiGetDictByKeyRequest, options?: RawAxiosRequestConfig): AxiosPromise<Dict> {
            return localVarFp.getDictByKey(requestParameters.key, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 列出所有字典项目
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        listDict(options?: RawAxiosRequestConfig): AxiosPromise<Array<Dict>> {
            return localVarFp.listDict(options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 更新字典项
         * @param {DictApiUpdateDictRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        updateDict(requestParameters: DictApiUpdateDictRequest, options?: RawAxiosRequestConfig): AxiosPromise<Dict> {
            return localVarFp.updateDict(requestParameters.key, requestParameters.dictSaveRequest, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 删除字典项
         * @param {DictApiUpdateDict1Request} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        updateDict1(requestParameters: DictApiUpdateDict1Request, options?: RawAxiosRequestConfig): AxiosPromise<boolean> {
            return localVarFp.updateDict1(requestParameters.key, options).then((request) => request(axios, basePath));
        },
    };
};

/**
 * Request parameters for createDict operation in DictApi.
 * @export
 * @interface DictApiCreateDictRequest
 */
export interface DictApiCreateDictRequest {
    /**
     * 
     * @type {DictSaveRequest}
     * @memberof DictApiCreateDict
     */
    readonly dictSaveRequest: DictSaveRequest
}

/**
 * Request parameters for getDictByKey operation in DictApi.
 * @export
 * @interface DictApiGetDictByKeyRequest
 */
export interface DictApiGetDictByKeyRequest {
    /**
     * 字典key
     * @type {string}
     * @memberof DictApiGetDictByKey
     */
    readonly key: string
}

/**
 * Request parameters for updateDict operation in DictApi.
 * @export
 * @interface DictApiUpdateDictRequest
 */
export interface DictApiUpdateDictRequest {
    /**
     * 
     * @type {string}
     * @memberof DictApiUpdateDict
     */
    readonly key: string

    /**
     * 
     * @type {DictSaveRequest}
     * @memberof DictApiUpdateDict
     */
    readonly dictSaveRequest: DictSaveRequest
}

/**
 * Request parameters for updateDict1 operation in DictApi.
 * @export
 * @interface DictApiUpdateDict1Request
 */
export interface DictApiUpdateDict1Request {
    /**
     * 
     * @type {string}
     * @memberof DictApiUpdateDict1
     */
    readonly key: string
}

/**
 * DictApi - object-oriented interface
 * @export
 * @class DictApi
 * @extends {BaseAPI}
 */
export class DictApi extends BaseAPI {
    /**
     * 
     * @summary 创建字典项
     * @param {DictApiCreateDictRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof DictApi
     */
    public createDict(requestParameters: DictApiCreateDictRequest, options?: RawAxiosRequestConfig) {
        return DictApiFp(this.configuration).createDict(requestParameters.dictSaveRequest, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 根据key或者字典项查询对应的值
     * @param {DictApiGetDictByKeyRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof DictApi
     */
    public getDictByKey(requestParameters: DictApiGetDictByKeyRequest, options?: RawAxiosRequestConfig) {
        return DictApiFp(this.configuration).getDictByKey(requestParameters.key, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 列出所有字典项目
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof DictApi
     */
    public listDict(options?: RawAxiosRequestConfig) {
        return DictApiFp(this.configuration).listDict(options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 更新字典项
     * @param {DictApiUpdateDictRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof DictApi
     */
    public updateDict(requestParameters: DictApiUpdateDictRequest, options?: RawAxiosRequestConfig) {
        return DictApiFp(this.configuration).updateDict(requestParameters.key, requestParameters.dictSaveRequest, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 删除字典项
     * @param {DictApiUpdateDict1Request} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof DictApi
     */
    public updateDict1(requestParameters: DictApiUpdateDict1Request, options?: RawAxiosRequestConfig) {
        return DictApiFp(this.configuration).updateDict1(requestParameters.key, options).then((request) => request(this.axios, this.basePath));
    }
}



/**
 * ErrorCodesApi - axios parameter creator
 * @export
 */
export const ErrorCodesApiAxiosParamCreator = function (configuration?: Configuration) {
    return {
        /**
         * 
         * @summary 获取错误码。
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getErrorCode: async (options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            const localVarPath = `/api/v1/error-codes`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
    }
};

/**
 * ErrorCodesApi - functional programming interface
 * @export
 */
export const ErrorCodesApiFp = function (configuration?: Configuration) {
    const localVarAxiosParamCreator = ErrorCodesApiAxiosParamCreator(configuration)
    return {
        /**
         * 
         * @summary 获取错误码。
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async getErrorCode(options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<{ [key: string]: string; }>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.getErrorCode(options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['ErrorCodesApi.getErrorCode']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
    }
};

/**
 * ErrorCodesApi - factory interface
 * @export
 */
export const ErrorCodesApiFactory = function (configuration?: Configuration, basePath?: string, axios?: AxiosInstance) {
    const localVarFp = ErrorCodesApiFp(configuration)
    return {
        /**
         * 
         * @summary 获取错误码。
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getErrorCode(options?: RawAxiosRequestConfig): AxiosPromise<{ [key: string]: string; }> {
            return localVarFp.getErrorCode(options).then((request) => request(axios, basePath));
        },
    };
};

/**
 * ErrorCodesApi - object-oriented interface
 * @export
 * @class ErrorCodesApi
 * @extends {BaseAPI}
 */
export class ErrorCodesApi extends BaseAPI {
    /**
     * 
     * @summary 获取错误码。
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof ErrorCodesApi
     */
    public getErrorCode(options?: RawAxiosRequestConfig) {
        return ErrorCodesApiFp(this.configuration).getErrorCode(options).then((request) => request(this.axios, this.basePath));
    }
}



/**
 * ItemExchangeApi - axios parameter creator
 * @export
 */
export const ItemExchangeApiAxiosParamCreator = function (configuration?: Configuration) {
    return {
        /**
         * 
         * @summary 管理员创建兑换活动
         * @param {LotteryExchangeActivity} lotteryExchangeActivity 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        createActivity: async (lotteryExchangeActivity: LotteryExchangeActivity, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'lotteryExchangeActivity' is not null or undefined
            assertParamExists('createActivity', 'lotteryExchangeActivity', lotteryExchangeActivity)
            const localVarPath = `/api/v1/exchange/admin/activities`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'POST', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            localVarHeaderParameter['Content-Type'] = 'application/json';

            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };
            localVarRequestOptions.data = serializeDataIfNeeded(lotteryExchangeActivity, localVarRequestOptions, configuration)

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 管理员删除兑换活动
         * @param {string} activityId 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        deleteActivity: async (activityId: string, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'activityId' is not null or undefined
            assertParamExists('deleteActivity', 'activityId', activityId)
            const localVarPath = `/api/v1/exchange/admin/activities/{activityId}`
                .replace(`{${"activityId"}}`, encodeURIComponent(String(activityId)));
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'DELETE', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 兑换奖品
         * @param {string} activityId 
         * @param {string} itemId 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        exchangeItem: async (activityId: string, itemId: string, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'activityId' is not null or undefined
            assertParamExists('exchangeItem', 'activityId', activityId)
            // verify required parameter 'itemId' is not null or undefined
            assertParamExists('exchangeItem', 'itemId', itemId)
            const localVarPath = `/api/v1/exchange/activities/{activityId}/item/{itemId}`
                .replace(`{${"activityId"}}`, encodeURIComponent(String(activityId)))
                .replace(`{${"itemId"}}`, encodeURIComponent(String(itemId)));
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'POST', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 填写用户兑换奖励地址
         * @param {string} recordId 
         * @param {Address} address 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        fillExchangeRecord: async (recordId: string, address: Address, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'recordId' is not null or undefined
            assertParamExists('fillExchangeRecord', 'recordId', recordId)
            // verify required parameter 'address' is not null or undefined
            assertParamExists('fillExchangeRecord', 'address', address)
            const localVarPath = `/api/v1/exchange/activities/user-record/{recordId}/address`
                .replace(`{${"recordId"}}`, encodeURIComponent(String(recordId)));
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'POST', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            localVarHeaderParameter['Content-Type'] = 'application/json';

            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };
            localVarRequestOptions.data = serializeDataIfNeeded(address, localVarRequestOptions, configuration)

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 管理员获取兑换活动列表
         * @param {number} offset 
         * @param {number} limit 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getActivities: async (offset: number, limit: number, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'offset' is not null or undefined
            assertParamExists('getActivities', 'offset', offset)
            // verify required parameter 'limit' is not null or undefined
            assertParamExists('getActivities', 'limit', limit)
            const localVarPath = `/api/v1/exchange/admin/activities`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)

            if (offset !== undefined) {
                localVarQueryParameter['offset'] = offset;
            }

            if (limit !== undefined) {
                localVarQueryParameter['limit'] = limit;
            }



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 获取指定活动信息
         * @param {string} activityId 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getActivity: async (activityId: string, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'activityId' is not null or undefined
            assertParamExists('getActivity', 'activityId', activityId)
            const localVarPath = `/api/v1/exchange/activities/{activityId}`
                .replace(`{${"activityId"}}`, encodeURIComponent(String(activityId)));
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 管理员获取兑换活动数量
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getActivityCount: async (options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            const localVarPath = `/api/v1/exchange/admin/activities/count`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 获取兑换记录数量
         * @param {string} activityId 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getExchangeRecordCount: async (activityId: string, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'activityId' is not null or undefined
            assertParamExists('getExchangeRecordCount', 'activityId', activityId)
            const localVarPath = `/api/v1/exchange/activities/{activityId}/record-count`
                .replace(`{${"activityId"}}`, encodeURIComponent(String(activityId)));
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 获取用户兑换记录
         * @param {string} activityId 
         * @param {number} offset 
         * @param {number} limit 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getExchangeRecords: async (activityId: string, offset: number, limit: number, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'activityId' is not null or undefined
            assertParamExists('getExchangeRecords', 'activityId', activityId)
            // verify required parameter 'offset' is not null or undefined
            assertParamExists('getExchangeRecords', 'offset', offset)
            // verify required parameter 'limit' is not null or undefined
            assertParamExists('getExchangeRecords', 'limit', limit)
            const localVarPath = `/api/v1/exchange/activities/{activityId}/user-records`
                .replace(`{${"activityId"}}`, encodeURIComponent(String(activityId)));
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)

            if (offset !== undefined) {
                localVarQueryParameter['offset'] = offset;
            }

            if (limit !== undefined) {
                localVarQueryParameter['limit'] = limit;
            }



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 管理员更新兑换活动
         * @param {string} activityId 
         * @param {LotteryExchangeActivity} lotteryExchangeActivity 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        updateActivity: async (activityId: string, lotteryExchangeActivity: LotteryExchangeActivity, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'activityId' is not null or undefined
            assertParamExists('updateActivity', 'activityId', activityId)
            // verify required parameter 'lotteryExchangeActivity' is not null or undefined
            assertParamExists('updateActivity', 'lotteryExchangeActivity', lotteryExchangeActivity)
            const localVarPath = `/api/v1/exchange/admin/activities/{activityId}`
                .replace(`{${"activityId"}}`, encodeURIComponent(String(activityId)));
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'PUT', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            localVarHeaderParameter['Content-Type'] = 'application/json';

            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };
            localVarRequestOptions.data = serializeDataIfNeeded(lotteryExchangeActivity, localVarRequestOptions, configuration)

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
    }
};

/**
 * ItemExchangeApi - functional programming interface
 * @export
 */
export const ItemExchangeApiFp = function (configuration?: Configuration) {
    const localVarAxiosParamCreator = ItemExchangeApiAxiosParamCreator(configuration)
    return {
        /**
         * 
         * @summary 管理员创建兑换活动
         * @param {LotteryExchangeActivity} lotteryExchangeActivity 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async createActivity(lotteryExchangeActivity: LotteryExchangeActivity, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<LotteryExchangeActivity>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.createActivity(lotteryExchangeActivity, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['ItemExchangeApi.createActivity']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 管理员删除兑换活动
         * @param {string} activityId 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async deleteActivity(activityId: string, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<void>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.deleteActivity(activityId, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['ItemExchangeApi.deleteActivity']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 兑换奖品
         * @param {string} activityId 
         * @param {string} itemId 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async exchangeItem(activityId: string, itemId: string, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<ExchangeItem>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.exchangeItem(activityId, itemId, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['ItemExchangeApi.exchangeItem']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 填写用户兑换奖励地址
         * @param {string} recordId 
         * @param {Address} address 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async fillExchangeRecord(recordId: string, address: Address, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<ExchangeRecord>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.fillExchangeRecord(recordId, address, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['ItemExchangeApi.fillExchangeRecord']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 管理员获取兑换活动列表
         * @param {number} offset 
         * @param {number} limit 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async getActivities(offset: number, limit: number, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<Array<LotteryExchangeActivity>>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.getActivities(offset, limit, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['ItemExchangeApi.getActivities']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 获取指定活动信息
         * @param {string} activityId 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async getActivity(activityId: string, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<LotteryExchangeActivity>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.getActivity(activityId, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['ItemExchangeApi.getActivity']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 管理员获取兑换活动数量
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async getActivityCount(options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<number>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.getActivityCount(options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['ItemExchangeApi.getActivityCount']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 获取兑换记录数量
         * @param {string} activityId 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async getExchangeRecordCount(activityId: string, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<number>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.getExchangeRecordCount(activityId, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['ItemExchangeApi.getExchangeRecordCount']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 获取用户兑换记录
         * @param {string} activityId 
         * @param {number} offset 
         * @param {number} limit 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async getExchangeRecords(activityId: string, offset: number, limit: number, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<Array<ExchangeRecord>>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.getExchangeRecords(activityId, offset, limit, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['ItemExchangeApi.getExchangeRecords']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 管理员更新兑换活动
         * @param {string} activityId 
         * @param {LotteryExchangeActivity} lotteryExchangeActivity 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async updateActivity(activityId: string, lotteryExchangeActivity: LotteryExchangeActivity, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<ExchangeActivity>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.updateActivity(activityId, lotteryExchangeActivity, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['ItemExchangeApi.updateActivity']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
    }
};

/**
 * ItemExchangeApi - factory interface
 * @export
 */
export const ItemExchangeApiFactory = function (configuration?: Configuration, basePath?: string, axios?: AxiosInstance) {
    const localVarFp = ItemExchangeApiFp(configuration)
    return {
        /**
         * 
         * @summary 管理员创建兑换活动
         * @param {ItemExchangeApiCreateActivityRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        createActivity(requestParameters: ItemExchangeApiCreateActivityRequest, options?: RawAxiosRequestConfig): AxiosPromise<LotteryExchangeActivity> {
            return localVarFp.createActivity(requestParameters.lotteryExchangeActivity, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 管理员删除兑换活动
         * @param {ItemExchangeApiDeleteActivityRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        deleteActivity(requestParameters: ItemExchangeApiDeleteActivityRequest, options?: RawAxiosRequestConfig): AxiosPromise<void> {
            return localVarFp.deleteActivity(requestParameters.activityId, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 兑换奖品
         * @param {ItemExchangeApiExchangeItemRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        exchangeItem(requestParameters: ItemExchangeApiExchangeItemRequest, options?: RawAxiosRequestConfig): AxiosPromise<ExchangeItem> {
            return localVarFp.exchangeItem(requestParameters.activityId, requestParameters.itemId, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 填写用户兑换奖励地址
         * @param {ItemExchangeApiFillExchangeRecordRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        fillExchangeRecord(requestParameters: ItemExchangeApiFillExchangeRecordRequest, options?: RawAxiosRequestConfig): AxiosPromise<ExchangeRecord> {
            return localVarFp.fillExchangeRecord(requestParameters.recordId, requestParameters.address, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 管理员获取兑换活动列表
         * @param {ItemExchangeApiGetActivitiesRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getActivities(requestParameters: ItemExchangeApiGetActivitiesRequest, options?: RawAxiosRequestConfig): AxiosPromise<Array<LotteryExchangeActivity>> {
            return localVarFp.getActivities(requestParameters.offset, requestParameters.limit, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 获取指定活动信息
         * @param {ItemExchangeApiGetActivityRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getActivity(requestParameters: ItemExchangeApiGetActivityRequest, options?: RawAxiosRequestConfig): AxiosPromise<LotteryExchangeActivity> {
            return localVarFp.getActivity(requestParameters.activityId, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 管理员获取兑换活动数量
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getActivityCount(options?: RawAxiosRequestConfig): AxiosPromise<number> {
            return localVarFp.getActivityCount(options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 获取兑换记录数量
         * @param {ItemExchangeApiGetExchangeRecordCountRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getExchangeRecordCount(requestParameters: ItemExchangeApiGetExchangeRecordCountRequest, options?: RawAxiosRequestConfig): AxiosPromise<number> {
            return localVarFp.getExchangeRecordCount(requestParameters.activityId, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 获取用户兑换记录
         * @param {ItemExchangeApiGetExchangeRecordsRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getExchangeRecords(requestParameters: ItemExchangeApiGetExchangeRecordsRequest, options?: RawAxiosRequestConfig): AxiosPromise<Array<ExchangeRecord>> {
            return localVarFp.getExchangeRecords(requestParameters.activityId, requestParameters.offset, requestParameters.limit, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 管理员更新兑换活动
         * @param {ItemExchangeApiUpdateActivityRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        updateActivity(requestParameters: ItemExchangeApiUpdateActivityRequest, options?: RawAxiosRequestConfig): AxiosPromise<ExchangeActivity> {
            return localVarFp.updateActivity(requestParameters.activityId, requestParameters.lotteryExchangeActivity, options).then((request) => request(axios, basePath));
        },
    };
};

/**
 * Request parameters for createActivity operation in ItemExchangeApi.
 * @export
 * @interface ItemExchangeApiCreateActivityRequest
 */
export interface ItemExchangeApiCreateActivityRequest {
    /**
     * 
     * @type {LotteryExchangeActivity}
     * @memberof ItemExchangeApiCreateActivity
     */
    readonly lotteryExchangeActivity: LotteryExchangeActivity
}

/**
 * Request parameters for deleteActivity operation in ItemExchangeApi.
 * @export
 * @interface ItemExchangeApiDeleteActivityRequest
 */
export interface ItemExchangeApiDeleteActivityRequest {
    /**
     * 
     * @type {string}
     * @memberof ItemExchangeApiDeleteActivity
     */
    readonly activityId: string
}

/**
 * Request parameters for exchangeItem operation in ItemExchangeApi.
 * @export
 * @interface ItemExchangeApiExchangeItemRequest
 */
export interface ItemExchangeApiExchangeItemRequest {
    /**
     * 
     * @type {string}
     * @memberof ItemExchangeApiExchangeItem
     */
    readonly activityId: string

    /**
     * 
     * @type {string}
     * @memberof ItemExchangeApiExchangeItem
     */
    readonly itemId: string
}

/**
 * Request parameters for fillExchangeRecord operation in ItemExchangeApi.
 * @export
 * @interface ItemExchangeApiFillExchangeRecordRequest
 */
export interface ItemExchangeApiFillExchangeRecordRequest {
    /**
     * 
     * @type {string}
     * @memberof ItemExchangeApiFillExchangeRecord
     */
    readonly recordId: string

    /**
     * 
     * @type {Address}
     * @memberof ItemExchangeApiFillExchangeRecord
     */
    readonly address: Address
}

/**
 * Request parameters for getActivities operation in ItemExchangeApi.
 * @export
 * @interface ItemExchangeApiGetActivitiesRequest
 */
export interface ItemExchangeApiGetActivitiesRequest {
    /**
     * 
     * @type {number}
     * @memberof ItemExchangeApiGetActivities
     */
    readonly offset: number

    /**
     * 
     * @type {number}
     * @memberof ItemExchangeApiGetActivities
     */
    readonly limit: number
}

/**
 * Request parameters for getActivity operation in ItemExchangeApi.
 * @export
 * @interface ItemExchangeApiGetActivityRequest
 */
export interface ItemExchangeApiGetActivityRequest {
    /**
     * 
     * @type {string}
     * @memberof ItemExchangeApiGetActivity
     */
    readonly activityId: string
}

/**
 * Request parameters for getExchangeRecordCount operation in ItemExchangeApi.
 * @export
 * @interface ItemExchangeApiGetExchangeRecordCountRequest
 */
export interface ItemExchangeApiGetExchangeRecordCountRequest {
    /**
     * 
     * @type {string}
     * @memberof ItemExchangeApiGetExchangeRecordCount
     */
    readonly activityId: string
}

/**
 * Request parameters for getExchangeRecords operation in ItemExchangeApi.
 * @export
 * @interface ItemExchangeApiGetExchangeRecordsRequest
 */
export interface ItemExchangeApiGetExchangeRecordsRequest {
    /**
     * 
     * @type {string}
     * @memberof ItemExchangeApiGetExchangeRecords
     */
    readonly activityId: string

    /**
     * 
     * @type {number}
     * @memberof ItemExchangeApiGetExchangeRecords
     */
    readonly offset: number

    /**
     * 
     * @type {number}
     * @memberof ItemExchangeApiGetExchangeRecords
     */
    readonly limit: number
}

/**
 * Request parameters for updateActivity operation in ItemExchangeApi.
 * @export
 * @interface ItemExchangeApiUpdateActivityRequest
 */
export interface ItemExchangeApiUpdateActivityRequest {
    /**
     * 
     * @type {string}
     * @memberof ItemExchangeApiUpdateActivity
     */
    readonly activityId: string

    /**
     * 
     * @type {LotteryExchangeActivity}
     * @memberof ItemExchangeApiUpdateActivity
     */
    readonly lotteryExchangeActivity: LotteryExchangeActivity
}

/**
 * ItemExchangeApi - object-oriented interface
 * @export
 * @class ItemExchangeApi
 * @extends {BaseAPI}
 */
export class ItemExchangeApi extends BaseAPI {
    /**
     * 
     * @summary 管理员创建兑换活动
     * @param {ItemExchangeApiCreateActivityRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof ItemExchangeApi
     */
    public createActivity(requestParameters: ItemExchangeApiCreateActivityRequest, options?: RawAxiosRequestConfig) {
        return ItemExchangeApiFp(this.configuration).createActivity(requestParameters.lotteryExchangeActivity, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 管理员删除兑换活动
     * @param {ItemExchangeApiDeleteActivityRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof ItemExchangeApi
     */
    public deleteActivity(requestParameters: ItemExchangeApiDeleteActivityRequest, options?: RawAxiosRequestConfig) {
        return ItemExchangeApiFp(this.configuration).deleteActivity(requestParameters.activityId, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 兑换奖品
     * @param {ItemExchangeApiExchangeItemRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof ItemExchangeApi
     */
    public exchangeItem(requestParameters: ItemExchangeApiExchangeItemRequest, options?: RawAxiosRequestConfig) {
        return ItemExchangeApiFp(this.configuration).exchangeItem(requestParameters.activityId, requestParameters.itemId, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 填写用户兑换奖励地址
     * @param {ItemExchangeApiFillExchangeRecordRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof ItemExchangeApi
     */
    public fillExchangeRecord(requestParameters: ItemExchangeApiFillExchangeRecordRequest, options?: RawAxiosRequestConfig) {
        return ItemExchangeApiFp(this.configuration).fillExchangeRecord(requestParameters.recordId, requestParameters.address, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 管理员获取兑换活动列表
     * @param {ItemExchangeApiGetActivitiesRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof ItemExchangeApi
     */
    public getActivities(requestParameters: ItemExchangeApiGetActivitiesRequest, options?: RawAxiosRequestConfig) {
        return ItemExchangeApiFp(this.configuration).getActivities(requestParameters.offset, requestParameters.limit, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 获取指定活动信息
     * @param {ItemExchangeApiGetActivityRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof ItemExchangeApi
     */
    public getActivity(requestParameters: ItemExchangeApiGetActivityRequest, options?: RawAxiosRequestConfig) {
        return ItemExchangeApiFp(this.configuration).getActivity(requestParameters.activityId, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 管理员获取兑换活动数量
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof ItemExchangeApi
     */
    public getActivityCount(options?: RawAxiosRequestConfig) {
        return ItemExchangeApiFp(this.configuration).getActivityCount(options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 获取兑换记录数量
     * @param {ItemExchangeApiGetExchangeRecordCountRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof ItemExchangeApi
     */
    public getExchangeRecordCount(requestParameters: ItemExchangeApiGetExchangeRecordCountRequest, options?: RawAxiosRequestConfig) {
        return ItemExchangeApiFp(this.configuration).getExchangeRecordCount(requestParameters.activityId, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 获取用户兑换记录
     * @param {ItemExchangeApiGetExchangeRecordsRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof ItemExchangeApi
     */
    public getExchangeRecords(requestParameters: ItemExchangeApiGetExchangeRecordsRequest, options?: RawAxiosRequestConfig) {
        return ItemExchangeApiFp(this.configuration).getExchangeRecords(requestParameters.activityId, requestParameters.offset, requestParameters.limit, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 管理员更新兑换活动
     * @param {ItemExchangeApiUpdateActivityRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof ItemExchangeApi
     */
    public updateActivity(requestParameters: ItemExchangeApiUpdateActivityRequest, options?: RawAxiosRequestConfig) {
        return ItemExchangeApiFp(this.configuration).updateActivity(requestParameters.activityId, requestParameters.lotteryExchangeActivity, options).then((request) => request(this.axios, this.basePath));
    }
}



/**
 * LibraryApi - axios parameter creator
 * @export
 */
export const LibraryApiAxiosParamCreator = function (configuration?: Configuration) {
    return {
        /**
         * 
         * @summary 创建素材资源
         * @param {CreateResourceRequest} createResourceRequest 
         * @param {string} [title] 
         * @param {string} [description] 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        createResource: async (createResourceRequest: CreateResourceRequest, title?: string, description?: string, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'createResourceRequest' is not null or undefined
            assertParamExists('createResource', 'createResourceRequest', createResourceRequest)
            const localVarPath = `/api/v1/ntes-library/resources`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'POST', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)

            if (title !== undefined) {
                localVarQueryParameter['title'] = title;
            }

            if (description !== undefined) {
                localVarQueryParameter['description'] = description;
            }



            localVarHeaderParameter['Content-Type'] = 'application/octet-stream';

            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };
            localVarRequestOptions.data = serializeDataIfNeeded(createResourceRequest, localVarRequestOptions, configuration)

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 删除素材资源
         * @param {string} id 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        deleteResource: async (id: string, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'id' is not null or undefined
            assertParamExists('deleteResource', 'id', id)
            const localVarPath = `/api/v1/ntes-library/resources/{id}`
                .replace(`{${"id"}}`, encodeURIComponent(String(id)));
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'DELETE', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 获取素材资源
         * @param {string} id 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getResource: async (id: string, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'id' is not null or undefined
            assertParamExists('getResource', 'id', id)
            const localVarPath = `/api/v1/ntes-library/resources/{id}`
                .replace(`{${"id"}}`, encodeURIComponent(String(id)));
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 搜索素材资源
         * @param {string} [query] 
         * @param {number} [offset] 
         * @param {number} [limit] 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getResources: async (query?: string, offset?: number, limit?: number, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            const localVarPath = `/api/v1/ntes-library/resources`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)

            if (query !== undefined) {
                localVarQueryParameter['query'] = query;
            }

            if (offset !== undefined) {
                localVarQueryParameter['offset'] = offset;
            }

            if (limit !== undefined) {
                localVarQueryParameter['limit'] = limit;
            }



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
    }
};

/**
 * LibraryApi - functional programming interface
 * @export
 */
export const LibraryApiFp = function (configuration?: Configuration) {
    const localVarAxiosParamCreator = LibraryApiAxiosParamCreator(configuration)
    return {
        /**
         * 
         * @summary 创建素材资源
         * @param {CreateResourceRequest} createResourceRequest 
         * @param {string} [title] 
         * @param {string} [description] 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async createResource(createResourceRequest: CreateResourceRequest, title?: string, description?: string, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<Resource>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.createResource(createResourceRequest, title, description, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['LibraryApi.createResource']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 删除素材资源
         * @param {string} id 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async deleteResource(id: string, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<void>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.deleteResource(id, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['LibraryApi.deleteResource']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 获取素材资源
         * @param {string} id 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async getResource(id: string, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<Resource>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.getResource(id, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['LibraryApi.getResource']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 搜索素材资源
         * @param {string} [query] 
         * @param {number} [offset] 
         * @param {number} [limit] 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async getResources(query?: string, offset?: number, limit?: number, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<Array<Resource>>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.getResources(query, offset, limit, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['LibraryApi.getResources']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
    }
};

/**
 * LibraryApi - factory interface
 * @export
 */
export const LibraryApiFactory = function (configuration?: Configuration, basePath?: string, axios?: AxiosInstance) {
    const localVarFp = LibraryApiFp(configuration)
    return {
        /**
         * 
         * @summary 创建素材资源
         * @param {LibraryApiCreateResourceRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        createResource(requestParameters: LibraryApiCreateResourceRequest, options?: RawAxiosRequestConfig): AxiosPromise<Resource> {
            return localVarFp.createResource(requestParameters.createResourceRequest, requestParameters.title, requestParameters.description, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 删除素材资源
         * @param {LibraryApiDeleteResourceRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        deleteResource(requestParameters: LibraryApiDeleteResourceRequest, options?: RawAxiosRequestConfig): AxiosPromise<void> {
            return localVarFp.deleteResource(requestParameters.id, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 获取素材资源
         * @param {LibraryApiGetResourceRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getResource(requestParameters: LibraryApiGetResourceRequest, options?: RawAxiosRequestConfig): AxiosPromise<Resource> {
            return localVarFp.getResource(requestParameters.id, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 搜索素材资源
         * @param {LibraryApiGetResourcesRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getResources(requestParameters: LibraryApiGetResourcesRequest = {}, options?: RawAxiosRequestConfig): AxiosPromise<Array<Resource>> {
            return localVarFp.getResources(requestParameters.query, requestParameters.offset, requestParameters.limit, options).then((request) => request(axios, basePath));
        },
    };
};

/**
 * Request parameters for createResource operation in LibraryApi.
 * @export
 * @interface LibraryApiCreateResourceRequest
 */
export interface LibraryApiCreateResourceRequest {
    /**
     * 
     * @type {CreateResourceRequest}
     * @memberof LibraryApiCreateResource
     */
    readonly createResourceRequest: CreateResourceRequest

    /**
     * 
     * @type {string}
     * @memberof LibraryApiCreateResource
     */
    readonly title?: string

    /**
     * 
     * @type {string}
     * @memberof LibraryApiCreateResource
     */
    readonly description?: string
}

/**
 * Request parameters for deleteResource operation in LibraryApi.
 * @export
 * @interface LibraryApiDeleteResourceRequest
 */
export interface LibraryApiDeleteResourceRequest {
    /**
     * 
     * @type {string}
     * @memberof LibraryApiDeleteResource
     */
    readonly id: string
}

/**
 * Request parameters for getResource operation in LibraryApi.
 * @export
 * @interface LibraryApiGetResourceRequest
 */
export interface LibraryApiGetResourceRequest {
    /**
     * 
     * @type {string}
     * @memberof LibraryApiGetResource
     */
    readonly id: string
}

/**
 * Request parameters for getResources operation in LibraryApi.
 * @export
 * @interface LibraryApiGetResourcesRequest
 */
export interface LibraryApiGetResourcesRequest {
    /**
     * 
     * @type {string}
     * @memberof LibraryApiGetResources
     */
    readonly query?: string

    /**
     * 
     * @type {number}
     * @memberof LibraryApiGetResources
     */
    readonly offset?: number

    /**
     * 
     * @type {number}
     * @memberof LibraryApiGetResources
     */
    readonly limit?: number
}

/**
 * LibraryApi - object-oriented interface
 * @export
 * @class LibraryApi
 * @extends {BaseAPI}
 */
export class LibraryApi extends BaseAPI {
    /**
     * 
     * @summary 创建素材资源
     * @param {LibraryApiCreateResourceRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof LibraryApi
     */
    public createResource(requestParameters: LibraryApiCreateResourceRequest, options?: RawAxiosRequestConfig) {
        return LibraryApiFp(this.configuration).createResource(requestParameters.createResourceRequest, requestParameters.title, requestParameters.description, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 删除素材资源
     * @param {LibraryApiDeleteResourceRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof LibraryApi
     */
    public deleteResource(requestParameters: LibraryApiDeleteResourceRequest, options?: RawAxiosRequestConfig) {
        return LibraryApiFp(this.configuration).deleteResource(requestParameters.id, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 获取素材资源
     * @param {LibraryApiGetResourceRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof LibraryApi
     */
    public getResource(requestParameters: LibraryApiGetResourceRequest, options?: RawAxiosRequestConfig) {
        return LibraryApiFp(this.configuration).getResource(requestParameters.id, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 搜索素材资源
     * @param {LibraryApiGetResourcesRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof LibraryApi
     */
    public getResources(requestParameters: LibraryApiGetResourcesRequest = {}, options?: RawAxiosRequestConfig) {
        return LibraryApiFp(this.configuration).getResources(requestParameters.query, requestParameters.offset, requestParameters.limit, options).then((request) => request(this.axios, this.basePath));
    }
}



/**
 * LottoApi - axios parameter creator
 * @export
 */
export const LottoApiAxiosParamCreator = function (configuration?: Configuration) {
    return {
        /**
         * 
         * @summary 手动领取奖品。
         * @param {string} itemId 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        claimLotteryItem: async (itemId: string, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'itemId' is not null or undefined
            assertParamExists('claimLotteryItem', 'itemId', itemId)
            const localVarPath = `/api/v1/lotto/items/{itemId}/claim`
                .replace(`{${"itemId"}}`, encodeURIComponent(String(itemId)));
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'POST', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 创建抽奖活动。
         * @param {CreateActivityRequest} createActivityRequest 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        createLotteryActivity: async (createActivityRequest: CreateActivityRequest, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'createActivityRequest' is not null or undefined
            assertParamExists('createLotteryActivity', 'createActivityRequest', createActivityRequest)
            const localVarPath = `/api/v1/lotto/activities`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'POST', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            localVarHeaderParameter['Content-Type'] = 'application/json';

            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };
            localVarRequestOptions.data = serializeDataIfNeeded(createActivityRequest, localVarRequestOptions, configuration)

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 删除抽奖活动。
         * @param {string} id 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        deleteLotteryActivity: async (id: string, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'id' is not null or undefined
            assertParamExists('deleteLotteryActivity', 'id', id)
            const localVarPath = `/api/v1/lotto/activities/{id}`
                .replace(`{${"id"}}`, encodeURIComponent(String(id)));
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'DELETE', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 获取活跃的抽奖活动列表。
         * @param {number} [offset] 
         * @param {number} [limit] 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getActiveLotteryActivities: async (offset?: number, limit?: number, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            const localVarPath = `/api/v1/lotto/active-activities`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)

            if (offset !== undefined) {
                localVarQueryParameter['offset'] = offset;
            }

            if (limit !== undefined) {
                localVarQueryParameter['limit'] = limit;
            }



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 获取指定 ID 的抽奖活动。
         * @param {string} id 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getActiveLotteryActivity: async (id: string, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'id' is not null or undefined
            assertParamExists('getActiveLotteryActivity', 'id', id)
            const localVarPath = `/api/v1/lotto/activity`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)

            if (id !== undefined) {
                localVarQueryParameter['id'] = id;
            }



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 获取抽奖活动列表。
         * @param {string} [query] 
         * @param {number} [offset] 
         * @param {number} [limit] 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getLotteryActivities: async (query?: string, offset?: number, limit?: number, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            const localVarPath = `/api/v1/lotto/activities`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)

            if (query !== undefined) {
                localVarQueryParameter['query'] = query;
            }

            if (offset !== undefined) {
                localVarQueryParameter['offset'] = offset;
            }

            if (limit !== undefined) {
                localVarQueryParameter['limit'] = limit;
            }



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 获取抽奖活动列表数量。
         * @param {string} [query] 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getLotteryActivitiesCount: async (query?: string, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            const localVarPath = `/api/v1/lotto/activities-count`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)

            if (query !== undefined) {
                localVarQueryParameter['query'] = query;
            }



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 根据 id 获取抽奖活动。
         * @param {string} id 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getLotteryActivity: async (id: string, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'id' is not null or undefined
            assertParamExists('getLotteryActivity', 'id', id)
            const localVarPath = `/api/v1/lotto/activities/{id}`
                .replace(`{${"id"}}`, encodeURIComponent(String(id)));
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 获取奖品上限规则列表。
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getLotteryBounds: async (options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            const localVarPath = `/api/v1/lotto/bounds`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 根据 id 获取抽奖活动的奖品消耗。（有库存上限设置的才会被记录）
         * @param {string} id 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getLotteryItemCount: async (id: string, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'id' is not null or undefined
            assertParamExists('getLotteryItemCount', 'id', id)
            const localVarPath = `/api/v1/lotto/activities/{id}/item-count`
                .replace(`{${"id"}}`, encodeURIComponent(String(id)));
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 获取奖品列表。
         * @param {string} [activityId] 
         * @param {number} [offset] 
         * @param {number} [limit] 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getLotteryItems: async (activityId?: string, offset?: number, limit?: number, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            const localVarPath = `/api/v1/lotto/items`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)

            if (activityId !== undefined) {
                localVarQueryParameter['activityId'] = activityId;
            }

            if (offset !== undefined) {
                localVarQueryParameter['offset'] = offset;
            }

            if (limit !== undefined) {
                localVarQueryParameter['limit'] = limit;
            }



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 获取奖品列表数量。
         * @param {string} [activityId] 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getLotteryItemsCount: async (activityId?: string, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            const localVarPath = `/api/v1/lotto/items-count`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)

            if (activityId !== undefined) {
                localVarQueryParameter['activityId'] = activityId;
            }



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 获取每日抽奖成功次数。
         * @param {Array<string>} [activityId] 
         * @param {string} [start] 
         * @param {string} [end] 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getLotteryItemsDailyCount: async (activityId?: Array<string>, start?: string, end?: string, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            const localVarPath = `/api/v1/lotto/roll-daily-count`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)

            if (activityId) {
                localVarQueryParameter['activityId'] = activityId;
            }

            if (start !== undefined) {
                localVarQueryParameter['start'] = (start as any instanceof Date) ?
                    (start as any).toISOString() :
                    start;
            }

            if (end !== undefined) {
                localVarQueryParameter['end'] = (end as any instanceof Date) ?
                    (end as any).toISOString() :
                    end;
            }



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 获取获奖列表 Excel。
         * @param {Array<string>} [activityId] 
         * @param {string} [start] 
         * @param {string} [end] 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getLotteryItemsExcel: async (activityId?: Array<string>, start?: string, end?: string, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            const localVarPath = `/api/v1/lotto/records/items-excel`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)

            if (activityId) {
                localVarQueryParameter['activityId'] = activityId;
            }

            if (start !== undefined) {
                localVarQueryParameter['start'] = (start as any instanceof Date) ?
                    (start as any).toISOString() :
                    start;
            }

            if (end !== undefined) {
                localVarQueryParameter['end'] = (end as any instanceof Date) ?
                    (end as any).toISOString() :
                    end;
            }



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 获取奖品类型列表。
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getProductTypes: async (options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            const localVarPath = `/api/v1/lotto/product-types`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 抽奖。
         * @param {string} id 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        lotteryRoll: async (id: string, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'id' is not null or undefined
            assertParamExists('lotteryRoll', 'id', id)
            const localVarPath = `/api/v1/lotto/activities/{id}/rolls`
                .replace(`{${"id"}}`, encodeURIComponent(String(id)));
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'POST', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 更新奖品地址。
         * @param {string} itemId 
         * @param {Address} address 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        setLotteryItemAddress: async (itemId: string, address: Address, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'itemId' is not null or undefined
            assertParamExists('setLotteryItemAddress', 'itemId', itemId)
            // verify required parameter 'address' is not null or undefined
            assertParamExists('setLotteryItemAddress', 'address', address)
            const localVarPath = `/api/v1/lotto/items/{itemId}/address`
                .replace(`{${"itemId"}}`, encodeURIComponent(String(itemId)));
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'PUT', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            localVarHeaderParameter['Content-Type'] = 'application/json';

            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };
            localVarRequestOptions.data = serializeDataIfNeeded(address, localVarRequestOptions, configuration)

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 更新抽奖活动。
         * @param {string} id 
         * @param {CreateActivityRequest} createActivityRequest 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        updateLotteryActivity: async (id: string, createActivityRequest: CreateActivityRequest, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'id' is not null or undefined
            assertParamExists('updateLotteryActivity', 'id', id)
            // verify required parameter 'createActivityRequest' is not null or undefined
            assertParamExists('updateLotteryActivity', 'createActivityRequest', createActivityRequest)
            const localVarPath = `/api/v1/lotto/activities/{id}`
                .replace(`{${"id"}}`, encodeURIComponent(String(id)));
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'PUT', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            localVarHeaderParameter['Content-Type'] = 'application/json';

            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };
            localVarRequestOptions.data = serializeDataIfNeeded(createActivityRequest, localVarRequestOptions, configuration)

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 记录抽奖活动的访问。
         * @param {string} id 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        viewActivity: async (id: string, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'id' is not null or undefined
            assertParamExists('viewActivity', 'id', id)
            const localVarPath = `/api/v1/lotto/activities/{id}/view`
                .replace(`{${"id"}}`, encodeURIComponent(String(id)));
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'POST', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
    }
};

/**
 * LottoApi - functional programming interface
 * @export
 */
export const LottoApiFp = function (configuration?: Configuration) {
    const localVarAxiosParamCreator = LottoApiAxiosParamCreator(configuration)
    return {
        /**
         * 
         * @summary 手动领取奖品。
         * @param {string} itemId 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async claimLotteryItem(itemId: string, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<UserLotteryItem>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.claimLotteryItem(itemId, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['LottoApi.claimLotteryItem']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 创建抽奖活动。
         * @param {CreateActivityRequest} createActivityRequest 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async createLotteryActivity(createActivityRequest: CreateActivityRequest, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<LotteryActivity>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.createLotteryActivity(createActivityRequest, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['LottoApi.createLotteryActivity']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 删除抽奖活动。
         * @param {string} id 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async deleteLotteryActivity(id: string, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<LotteryActivity>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.deleteLotteryActivity(id, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['LottoApi.deleteLotteryActivity']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 获取活跃的抽奖活动列表。
         * @param {number} [offset] 
         * @param {number} [limit] 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async getActiveLotteryActivities(offset?: number, limit?: number, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<Array<ActiveActivity>>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.getActiveLotteryActivities(offset, limit, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['LottoApi.getActiveLotteryActivities']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 获取指定 ID 的抽奖活动。
         * @param {string} id 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async getActiveLotteryActivity(id: string, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<ActiveActivity>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.getActiveLotteryActivity(id, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['LottoApi.getActiveLotteryActivity']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 获取抽奖活动列表。
         * @param {string} [query] 
         * @param {number} [offset] 
         * @param {number} [limit] 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async getLotteryActivities(query?: string, offset?: number, limit?: number, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<Array<LotteryActivity>>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.getLotteryActivities(query, offset, limit, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['LottoApi.getLotteryActivities']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 获取抽奖活动列表数量。
         * @param {string} [query] 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async getLotteryActivitiesCount(query?: string, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<number>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.getLotteryActivitiesCount(query, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['LottoApi.getLotteryActivitiesCount']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 根据 id 获取抽奖活动。
         * @param {string} id 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async getLotteryActivity(id: string, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<LotteryActivity>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.getLotteryActivity(id, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['LottoApi.getLotteryActivity']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 获取奖品上限规则列表。
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async getLotteryBounds(options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<Array<Bound>>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.getLotteryBounds(options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['LottoApi.getLotteryBounds']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 根据 id 获取抽奖活动的奖品消耗。（有库存上限设置的才会被记录）
         * @param {string} id 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async getLotteryItemCount(id: string, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<{ [key: string]: number; }>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.getLotteryItemCount(id, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['LottoApi.getLotteryItemCount']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 获取奖品列表。
         * @param {string} [activityId] 
         * @param {number} [offset] 
         * @param {number} [limit] 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async getLotteryItems(activityId?: string, offset?: number, limit?: number, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<Array<UserLotteryItem>>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.getLotteryItems(activityId, offset, limit, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['LottoApi.getLotteryItems']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 获取奖品列表数量。
         * @param {string} [activityId] 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async getLotteryItemsCount(activityId?: string, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<number>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.getLotteryItemsCount(activityId, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['LottoApi.getLotteryItemsCount']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 获取每日抽奖成功次数。
         * @param {Array<string>} [activityId] 
         * @param {string} [start] 
         * @param {string} [end] 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async getLotteryItemsDailyCount(activityId?: Array<string>, start?: string, end?: string, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<Array<DailyRollCount>>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.getLotteryItemsDailyCount(activityId, start, end, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['LottoApi.getLotteryItemsDailyCount']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 获取获奖列表 Excel。
         * @param {Array<string>} [activityId] 
         * @param {string} [start] 
         * @param {string} [end] 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async getLotteryItemsExcel(activityId?: Array<string>, start?: string, end?: string, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<void>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.getLotteryItemsExcel(activityId, start, end, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['LottoApi.getLotteryItemsExcel']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 获取奖品类型列表。
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async getProductTypes(options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<Array<ProductType>>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.getProductTypes(options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['LottoApi.getProductTypes']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 抽奖。
         * @param {string} id 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async lotteryRoll(id: string, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<UserLotteryItem>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.lotteryRoll(id, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['LottoApi.lotteryRoll']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 更新奖品地址。
         * @param {string} itemId 
         * @param {Address} address 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async setLotteryItemAddress(itemId: string, address: Address, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<void>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.setLotteryItemAddress(itemId, address, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['LottoApi.setLotteryItemAddress']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 更新抽奖活动。
         * @param {string} id 
         * @param {CreateActivityRequest} createActivityRequest 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async updateLotteryActivity(id: string, createActivityRequest: CreateActivityRequest, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<LotteryActivity>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.updateLotteryActivity(id, createActivityRequest, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['LottoApi.updateLotteryActivity']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 记录抽奖活动的访问。
         * @param {string} id 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async viewActivity(id: string, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<void>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.viewActivity(id, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['LottoApi.viewActivity']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
    }
};

/**
 * LottoApi - factory interface
 * @export
 */
export const LottoApiFactory = function (configuration?: Configuration, basePath?: string, axios?: AxiosInstance) {
    const localVarFp = LottoApiFp(configuration)
    return {
        /**
         * 
         * @summary 手动领取奖品。
         * @param {LottoApiClaimLotteryItemRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        claimLotteryItem(requestParameters: LottoApiClaimLotteryItemRequest, options?: RawAxiosRequestConfig): AxiosPromise<UserLotteryItem> {
            return localVarFp.claimLotteryItem(requestParameters.itemId, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 创建抽奖活动。
         * @param {LottoApiCreateLotteryActivityRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        createLotteryActivity(requestParameters: LottoApiCreateLotteryActivityRequest, options?: RawAxiosRequestConfig): AxiosPromise<LotteryActivity> {
            return localVarFp.createLotteryActivity(requestParameters.createActivityRequest, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 删除抽奖活动。
         * @param {LottoApiDeleteLotteryActivityRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        deleteLotteryActivity(requestParameters: LottoApiDeleteLotteryActivityRequest, options?: RawAxiosRequestConfig): AxiosPromise<LotteryActivity> {
            return localVarFp.deleteLotteryActivity(requestParameters.id, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 获取活跃的抽奖活动列表。
         * @param {LottoApiGetActiveLotteryActivitiesRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getActiveLotteryActivities(requestParameters: LottoApiGetActiveLotteryActivitiesRequest = {}, options?: RawAxiosRequestConfig): AxiosPromise<Array<ActiveActivity>> {
            return localVarFp.getActiveLotteryActivities(requestParameters.offset, requestParameters.limit, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 获取指定 ID 的抽奖活动。
         * @param {LottoApiGetActiveLotteryActivityRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getActiveLotteryActivity(requestParameters: LottoApiGetActiveLotteryActivityRequest, options?: RawAxiosRequestConfig): AxiosPromise<ActiveActivity> {
            return localVarFp.getActiveLotteryActivity(requestParameters.id, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 获取抽奖活动列表。
         * @param {LottoApiGetLotteryActivitiesRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getLotteryActivities(requestParameters: LottoApiGetLotteryActivitiesRequest = {}, options?: RawAxiosRequestConfig): AxiosPromise<Array<LotteryActivity>> {
            return localVarFp.getLotteryActivities(requestParameters.query, requestParameters.offset, requestParameters.limit, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 获取抽奖活动列表数量。
         * @param {LottoApiGetLotteryActivitiesCountRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getLotteryActivitiesCount(requestParameters: LottoApiGetLotteryActivitiesCountRequest = {}, options?: RawAxiosRequestConfig): AxiosPromise<number> {
            return localVarFp.getLotteryActivitiesCount(requestParameters.query, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 根据 id 获取抽奖活动。
         * @param {LottoApiGetLotteryActivityRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getLotteryActivity(requestParameters: LottoApiGetLotteryActivityRequest, options?: RawAxiosRequestConfig): AxiosPromise<LotteryActivity> {
            return localVarFp.getLotteryActivity(requestParameters.id, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 获取奖品上限规则列表。
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getLotteryBounds(options?: RawAxiosRequestConfig): AxiosPromise<Array<Bound>> {
            return localVarFp.getLotteryBounds(options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 根据 id 获取抽奖活动的奖品消耗。（有库存上限设置的才会被记录）
         * @param {LottoApiGetLotteryItemCountRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getLotteryItemCount(requestParameters: LottoApiGetLotteryItemCountRequest, options?: RawAxiosRequestConfig): AxiosPromise<{ [key: string]: number; }> {
            return localVarFp.getLotteryItemCount(requestParameters.id, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 获取奖品列表。
         * @param {LottoApiGetLotteryItemsRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getLotteryItems(requestParameters: LottoApiGetLotteryItemsRequest = {}, options?: RawAxiosRequestConfig): AxiosPromise<Array<UserLotteryItem>> {
            return localVarFp.getLotteryItems(requestParameters.activityId, requestParameters.offset, requestParameters.limit, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 获取奖品列表数量。
         * @param {LottoApiGetLotteryItemsCountRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getLotteryItemsCount(requestParameters: LottoApiGetLotteryItemsCountRequest = {}, options?: RawAxiosRequestConfig): AxiosPromise<number> {
            return localVarFp.getLotteryItemsCount(requestParameters.activityId, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 获取每日抽奖成功次数。
         * @param {LottoApiGetLotteryItemsDailyCountRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getLotteryItemsDailyCount(requestParameters: LottoApiGetLotteryItemsDailyCountRequest = {}, options?: RawAxiosRequestConfig): AxiosPromise<Array<DailyRollCount>> {
            return localVarFp.getLotteryItemsDailyCount(requestParameters.activityId, requestParameters.start, requestParameters.end, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 获取获奖列表 Excel。
         * @param {LottoApiGetLotteryItemsExcelRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getLotteryItemsExcel(requestParameters: LottoApiGetLotteryItemsExcelRequest = {}, options?: RawAxiosRequestConfig): AxiosPromise<void> {
            return localVarFp.getLotteryItemsExcel(requestParameters.activityId, requestParameters.start, requestParameters.end, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 获取奖品类型列表。
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getProductTypes(options?: RawAxiosRequestConfig): AxiosPromise<Array<ProductType>> {
            return localVarFp.getProductTypes(options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 抽奖。
         * @param {LottoApiLotteryRollRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        lotteryRoll(requestParameters: LottoApiLotteryRollRequest, options?: RawAxiosRequestConfig): AxiosPromise<UserLotteryItem> {
            return localVarFp.lotteryRoll(requestParameters.id, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 更新奖品地址。
         * @param {LottoApiSetLotteryItemAddressRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        setLotteryItemAddress(requestParameters: LottoApiSetLotteryItemAddressRequest, options?: RawAxiosRequestConfig): AxiosPromise<void> {
            return localVarFp.setLotteryItemAddress(requestParameters.itemId, requestParameters.address, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 更新抽奖活动。
         * @param {LottoApiUpdateLotteryActivityRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        updateLotteryActivity(requestParameters: LottoApiUpdateLotteryActivityRequest, options?: RawAxiosRequestConfig): AxiosPromise<LotteryActivity> {
            return localVarFp.updateLotteryActivity(requestParameters.id, requestParameters.createActivityRequest, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 记录抽奖活动的访问。
         * @param {LottoApiViewActivityRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        viewActivity(requestParameters: LottoApiViewActivityRequest, options?: RawAxiosRequestConfig): AxiosPromise<void> {
            return localVarFp.viewActivity(requestParameters.id, options).then((request) => request(axios, basePath));
        },
    };
};

/**
 * Request parameters for claimLotteryItem operation in LottoApi.
 * @export
 * @interface LottoApiClaimLotteryItemRequest
 */
export interface LottoApiClaimLotteryItemRequest {
    /**
     * 
     * @type {string}
     * @memberof LottoApiClaimLotteryItem
     */
    readonly itemId: string
}

/**
 * Request parameters for createLotteryActivity operation in LottoApi.
 * @export
 * @interface LottoApiCreateLotteryActivityRequest
 */
export interface LottoApiCreateLotteryActivityRequest {
    /**
     * 
     * @type {CreateActivityRequest}
     * @memberof LottoApiCreateLotteryActivity
     */
    readonly createActivityRequest: CreateActivityRequest
}

/**
 * Request parameters for deleteLotteryActivity operation in LottoApi.
 * @export
 * @interface LottoApiDeleteLotteryActivityRequest
 */
export interface LottoApiDeleteLotteryActivityRequest {
    /**
     * 
     * @type {string}
     * @memberof LottoApiDeleteLotteryActivity
     */
    readonly id: string
}

/**
 * Request parameters for getActiveLotteryActivities operation in LottoApi.
 * @export
 * @interface LottoApiGetActiveLotteryActivitiesRequest
 */
export interface LottoApiGetActiveLotteryActivitiesRequest {
    /**
     * 
     * @type {number}
     * @memberof LottoApiGetActiveLotteryActivities
     */
    readonly offset?: number

    /**
     * 
     * @type {number}
     * @memberof LottoApiGetActiveLotteryActivities
     */
    readonly limit?: number
}

/**
 * Request parameters for getActiveLotteryActivity operation in LottoApi.
 * @export
 * @interface LottoApiGetActiveLotteryActivityRequest
 */
export interface LottoApiGetActiveLotteryActivityRequest {
    /**
     * 
     * @type {string}
     * @memberof LottoApiGetActiveLotteryActivity
     */
    readonly id: string
}

/**
 * Request parameters for getLotteryActivities operation in LottoApi.
 * @export
 * @interface LottoApiGetLotteryActivitiesRequest
 */
export interface LottoApiGetLotteryActivitiesRequest {
    /**
     * 
     * @type {string}
     * @memberof LottoApiGetLotteryActivities
     */
    readonly query?: string

    /**
     * 
     * @type {number}
     * @memberof LottoApiGetLotteryActivities
     */
    readonly offset?: number

    /**
     * 
     * @type {number}
     * @memberof LottoApiGetLotteryActivities
     */
    readonly limit?: number
}

/**
 * Request parameters for getLotteryActivitiesCount operation in LottoApi.
 * @export
 * @interface LottoApiGetLotteryActivitiesCountRequest
 */
export interface LottoApiGetLotteryActivitiesCountRequest {
    /**
     * 
     * @type {string}
     * @memberof LottoApiGetLotteryActivitiesCount
     */
    readonly query?: string
}

/**
 * Request parameters for getLotteryActivity operation in LottoApi.
 * @export
 * @interface LottoApiGetLotteryActivityRequest
 */
export interface LottoApiGetLotteryActivityRequest {
    /**
     * 
     * @type {string}
     * @memberof LottoApiGetLotteryActivity
     */
    readonly id: string
}

/**
 * Request parameters for getLotteryItemCount operation in LottoApi.
 * @export
 * @interface LottoApiGetLotteryItemCountRequest
 */
export interface LottoApiGetLotteryItemCountRequest {
    /**
     * 
     * @type {string}
     * @memberof LottoApiGetLotteryItemCount
     */
    readonly id: string
}

/**
 * Request parameters for getLotteryItems operation in LottoApi.
 * @export
 * @interface LottoApiGetLotteryItemsRequest
 */
export interface LottoApiGetLotteryItemsRequest {
    /**
     * 
     * @type {string}
     * @memberof LottoApiGetLotteryItems
     */
    readonly activityId?: string

    /**
     * 
     * @type {number}
     * @memberof LottoApiGetLotteryItems
     */
    readonly offset?: number

    /**
     * 
     * @type {number}
     * @memberof LottoApiGetLotteryItems
     */
    readonly limit?: number
}

/**
 * Request parameters for getLotteryItemsCount operation in LottoApi.
 * @export
 * @interface LottoApiGetLotteryItemsCountRequest
 */
export interface LottoApiGetLotteryItemsCountRequest {
    /**
     * 
     * @type {string}
     * @memberof LottoApiGetLotteryItemsCount
     */
    readonly activityId?: string
}

/**
 * Request parameters for getLotteryItemsDailyCount operation in LottoApi.
 * @export
 * @interface LottoApiGetLotteryItemsDailyCountRequest
 */
export interface LottoApiGetLotteryItemsDailyCountRequest {
    /**
     * 
     * @type {Array<string>}
     * @memberof LottoApiGetLotteryItemsDailyCount
     */
    readonly activityId?: Array<string>

    /**
     * 
     * @type {string}
     * @memberof LottoApiGetLotteryItemsDailyCount
     */
    readonly start?: string

    /**
     * 
     * @type {string}
     * @memberof LottoApiGetLotteryItemsDailyCount
     */
    readonly end?: string
}

/**
 * Request parameters for getLotteryItemsExcel operation in LottoApi.
 * @export
 * @interface LottoApiGetLotteryItemsExcelRequest
 */
export interface LottoApiGetLotteryItemsExcelRequest {
    /**
     * 
     * @type {Array<string>}
     * @memberof LottoApiGetLotteryItemsExcel
     */
    readonly activityId?: Array<string>

    /**
     * 
     * @type {string}
     * @memberof LottoApiGetLotteryItemsExcel
     */
    readonly start?: string

    /**
     * 
     * @type {string}
     * @memberof LottoApiGetLotteryItemsExcel
     */
    readonly end?: string
}

/**
 * Request parameters for lotteryRoll operation in LottoApi.
 * @export
 * @interface LottoApiLotteryRollRequest
 */
export interface LottoApiLotteryRollRequest {
    /**
     * 
     * @type {string}
     * @memberof LottoApiLotteryRoll
     */
    readonly id: string
}

/**
 * Request parameters for setLotteryItemAddress operation in LottoApi.
 * @export
 * @interface LottoApiSetLotteryItemAddressRequest
 */
export interface LottoApiSetLotteryItemAddressRequest {
    /**
     * 
     * @type {string}
     * @memberof LottoApiSetLotteryItemAddress
     */
    readonly itemId: string

    /**
     * 
     * @type {Address}
     * @memberof LottoApiSetLotteryItemAddress
     */
    readonly address: Address
}

/**
 * Request parameters for updateLotteryActivity operation in LottoApi.
 * @export
 * @interface LottoApiUpdateLotteryActivityRequest
 */
export interface LottoApiUpdateLotteryActivityRequest {
    /**
     * 
     * @type {string}
     * @memberof LottoApiUpdateLotteryActivity
     */
    readonly id: string

    /**
     * 
     * @type {CreateActivityRequest}
     * @memberof LottoApiUpdateLotteryActivity
     */
    readonly createActivityRequest: CreateActivityRequest
}

/**
 * Request parameters for viewActivity operation in LottoApi.
 * @export
 * @interface LottoApiViewActivityRequest
 */
export interface LottoApiViewActivityRequest {
    /**
     * 
     * @type {string}
     * @memberof LottoApiViewActivity
     */
    readonly id: string
}

/**
 * LottoApi - object-oriented interface
 * @export
 * @class LottoApi
 * @extends {BaseAPI}
 */
export class LottoApi extends BaseAPI {
    /**
     * 
     * @summary 手动领取奖品。
     * @param {LottoApiClaimLotteryItemRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof LottoApi
     */
    public claimLotteryItem(requestParameters: LottoApiClaimLotteryItemRequest, options?: RawAxiosRequestConfig) {
        return LottoApiFp(this.configuration).claimLotteryItem(requestParameters.itemId, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 创建抽奖活动。
     * @param {LottoApiCreateLotteryActivityRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof LottoApi
     */
    public createLotteryActivity(requestParameters: LottoApiCreateLotteryActivityRequest, options?: RawAxiosRequestConfig) {
        return LottoApiFp(this.configuration).createLotteryActivity(requestParameters.createActivityRequest, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 删除抽奖活动。
     * @param {LottoApiDeleteLotteryActivityRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof LottoApi
     */
    public deleteLotteryActivity(requestParameters: LottoApiDeleteLotteryActivityRequest, options?: RawAxiosRequestConfig) {
        return LottoApiFp(this.configuration).deleteLotteryActivity(requestParameters.id, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 获取活跃的抽奖活动列表。
     * @param {LottoApiGetActiveLotteryActivitiesRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof LottoApi
     */
    public getActiveLotteryActivities(requestParameters: LottoApiGetActiveLotteryActivitiesRequest = {}, options?: RawAxiosRequestConfig) {
        return LottoApiFp(this.configuration).getActiveLotteryActivities(requestParameters.offset, requestParameters.limit, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 获取指定 ID 的抽奖活动。
     * @param {LottoApiGetActiveLotteryActivityRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof LottoApi
     */
    public getActiveLotteryActivity(requestParameters: LottoApiGetActiveLotteryActivityRequest, options?: RawAxiosRequestConfig) {
        return LottoApiFp(this.configuration).getActiveLotteryActivity(requestParameters.id, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 获取抽奖活动列表。
     * @param {LottoApiGetLotteryActivitiesRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof LottoApi
     */
    public getLotteryActivities(requestParameters: LottoApiGetLotteryActivitiesRequest = {}, options?: RawAxiosRequestConfig) {
        return LottoApiFp(this.configuration).getLotteryActivities(requestParameters.query, requestParameters.offset, requestParameters.limit, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 获取抽奖活动列表数量。
     * @param {LottoApiGetLotteryActivitiesCountRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof LottoApi
     */
    public getLotteryActivitiesCount(requestParameters: LottoApiGetLotteryActivitiesCountRequest = {}, options?: RawAxiosRequestConfig) {
        return LottoApiFp(this.configuration).getLotteryActivitiesCount(requestParameters.query, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 根据 id 获取抽奖活动。
     * @param {LottoApiGetLotteryActivityRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof LottoApi
     */
    public getLotteryActivity(requestParameters: LottoApiGetLotteryActivityRequest, options?: RawAxiosRequestConfig) {
        return LottoApiFp(this.configuration).getLotteryActivity(requestParameters.id, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 获取奖品上限规则列表。
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof LottoApi
     */
    public getLotteryBounds(options?: RawAxiosRequestConfig) {
        return LottoApiFp(this.configuration).getLotteryBounds(options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 根据 id 获取抽奖活动的奖品消耗。（有库存上限设置的才会被记录）
     * @param {LottoApiGetLotteryItemCountRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof LottoApi
     */
    public getLotteryItemCount(requestParameters: LottoApiGetLotteryItemCountRequest, options?: RawAxiosRequestConfig) {
        return LottoApiFp(this.configuration).getLotteryItemCount(requestParameters.id, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 获取奖品列表。
     * @param {LottoApiGetLotteryItemsRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof LottoApi
     */
    public getLotteryItems(requestParameters: LottoApiGetLotteryItemsRequest = {}, options?: RawAxiosRequestConfig) {
        return LottoApiFp(this.configuration).getLotteryItems(requestParameters.activityId, requestParameters.offset, requestParameters.limit, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 获取奖品列表数量。
     * @param {LottoApiGetLotteryItemsCountRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof LottoApi
     */
    public getLotteryItemsCount(requestParameters: LottoApiGetLotteryItemsCountRequest = {}, options?: RawAxiosRequestConfig) {
        return LottoApiFp(this.configuration).getLotteryItemsCount(requestParameters.activityId, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 获取每日抽奖成功次数。
     * @param {LottoApiGetLotteryItemsDailyCountRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof LottoApi
     */
    public getLotteryItemsDailyCount(requestParameters: LottoApiGetLotteryItemsDailyCountRequest = {}, options?: RawAxiosRequestConfig) {
        return LottoApiFp(this.configuration).getLotteryItemsDailyCount(requestParameters.activityId, requestParameters.start, requestParameters.end, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 获取获奖列表 Excel。
     * @param {LottoApiGetLotteryItemsExcelRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof LottoApi
     */
    public getLotteryItemsExcel(requestParameters: LottoApiGetLotteryItemsExcelRequest = {}, options?: RawAxiosRequestConfig) {
        return LottoApiFp(this.configuration).getLotteryItemsExcel(requestParameters.activityId, requestParameters.start, requestParameters.end, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 获取奖品类型列表。
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof LottoApi
     */
    public getProductTypes(options?: RawAxiosRequestConfig) {
        return LottoApiFp(this.configuration).getProductTypes(options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 抽奖。
     * @param {LottoApiLotteryRollRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof LottoApi
     */
    public lotteryRoll(requestParameters: LottoApiLotteryRollRequest, options?: RawAxiosRequestConfig) {
        return LottoApiFp(this.configuration).lotteryRoll(requestParameters.id, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 更新奖品地址。
     * @param {LottoApiSetLotteryItemAddressRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof LottoApi
     */
    public setLotteryItemAddress(requestParameters: LottoApiSetLotteryItemAddressRequest, options?: RawAxiosRequestConfig) {
        return LottoApiFp(this.configuration).setLotteryItemAddress(requestParameters.itemId, requestParameters.address, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 更新抽奖活动。
     * @param {LottoApiUpdateLotteryActivityRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof LottoApi
     */
    public updateLotteryActivity(requestParameters: LottoApiUpdateLotteryActivityRequest, options?: RawAxiosRequestConfig) {
        return LottoApiFp(this.configuration).updateLotteryActivity(requestParameters.id, requestParameters.createActivityRequest, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 记录抽奖活动的访问。
     * @param {LottoApiViewActivityRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof LottoApi
     */
    public viewActivity(requestParameters: LottoApiViewActivityRequest, options?: RawAxiosRequestConfig) {
        return LottoApiFp(this.configuration).viewActivity(requestParameters.id, options).then((request) => request(this.axios, this.basePath));
    }
}



/**
 * LsdmxAuthQaApi - axios parameter creator
 * @export
 */
export const LsdmxAuthQaApiAxiosParamCreator = function (configuration?: Configuration) {
    return {
        /**
         * 
         * @summary 管理员生成免登 URL。
         * @param {string} type 
         * @param {CreateUrlRequest} createUrlRequest 
         * @param {string} [channel] 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        createUrsToken3: async (type: string, createUrlRequest: CreateUrlRequest, channel?: string, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'type' is not null or undefined
            assertParamExists('createUrsToken3', 'type', type)
            // verify required parameter 'createUrlRequest' is not null or undefined
            assertParamExists('createUrsToken3', 'createUrlRequest', createUrlRequest)
            const localVarPath = `/api/v1/ntes-lsdmx/qa/url`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'POST', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)

            if (type !== undefined) {
                localVarQueryParameter['type'] = type;
            }

            if (channel !== undefined) {
                localVarQueryParameter['channel'] = channel;
            }



            localVarHeaderParameter['Content-Type'] = 'application/json';

            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };
            localVarRequestOptions.data = serializeDataIfNeeded(createUrlRequest, localVarRequestOptions, configuration)

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
    }
};

/**
 * LsdmxAuthQaApi - functional programming interface
 * @export
 */
export const LsdmxAuthQaApiFp = function (configuration?: Configuration) {
    const localVarAxiosParamCreator = LsdmxAuthQaApiAxiosParamCreator(configuration)
    return {
        /**
         * 
         * @summary 管理员生成免登 URL。
         * @param {string} type 
         * @param {CreateUrlRequest} createUrlRequest 
         * @param {string} [channel] 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async createUrsToken3(type: string, createUrlRequest: CreateUrlRequest, channel?: string, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<string>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.createUrsToken3(type, createUrlRequest, channel, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['LsdmxAuthQaApi.createUrsToken3']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
    }
};

/**
 * LsdmxAuthQaApi - factory interface
 * @export
 */
export const LsdmxAuthQaApiFactory = function (configuration?: Configuration, basePath?: string, axios?: AxiosInstance) {
    const localVarFp = LsdmxAuthQaApiFp(configuration)
    return {
        /**
         * 
         * @summary 管理员生成免登 URL。
         * @param {LsdmxAuthQaApiCreateUrsToken3Request} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        createUrsToken3(requestParameters: LsdmxAuthQaApiCreateUrsToken3Request, options?: RawAxiosRequestConfig): AxiosPromise<string> {
            return localVarFp.createUrsToken3(requestParameters.type, requestParameters.createUrlRequest, requestParameters.channel, options).then((request) => request(axios, basePath));
        },
    };
};

/**
 * Request parameters for createUrsToken3 operation in LsdmxAuthQaApi.
 * @export
 * @interface LsdmxAuthQaApiCreateUrsToken3Request
 */
export interface LsdmxAuthQaApiCreateUrsToken3Request {
    /**
     * 
     * @type {string}
     * @memberof LsdmxAuthQaApiCreateUrsToken3
     */
    readonly type: string

    /**
     * 
     * @type {CreateUrlRequest}
     * @memberof LsdmxAuthQaApiCreateUrsToken3
     */
    readonly createUrlRequest: CreateUrlRequest

    /**
     * 
     * @type {string}
     * @memberof LsdmxAuthQaApiCreateUrsToken3
     */
    readonly channel?: string
}

/**
 * LsdmxAuthQaApi - object-oriented interface
 * @export
 * @class LsdmxAuthQaApi
 * @extends {BaseAPI}
 */
export class LsdmxAuthQaApi extends BaseAPI {
    /**
     * 
     * @summary 管理员生成免登 URL。
     * @param {LsdmxAuthQaApiCreateUrsToken3Request} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof LsdmxAuthQaApi
     */
    public createUrsToken3(requestParameters: LsdmxAuthQaApiCreateUrsToken3Request, options?: RawAxiosRequestConfig) {
        return LsdmxAuthQaApiFp(this.configuration).createUrsToken3(requestParameters.type, requestParameters.createUrlRequest, requestParameters.channel, options).then((request) => request(this.axios, this.basePath));
    }
}



/**
 * LsdmxAuthURLApi - axios parameter creator
 * @export
 */
export const LsdmxAuthURLApiAxiosParamCreator = function (configuration?: Configuration) {
    return {
        /**
         * 
         * @summary 生成免登 URL
         * @param {string} type 
         * @param {string} xAppId 应用ID
         * @param {string} xAppSignature 应用签名
         * @param {string} xAppDate 应用时间戳
         * @param {CreateUrlRequest} createUrlRequest 
         * @param {string} [channel] 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        lsdmxGenerateUrl: async (type: string, xAppId: string, xAppSignature: string, xAppDate: string, createUrlRequest: CreateUrlRequest, channel?: string, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'type' is not null or undefined
            assertParamExists('lsdmxGenerateUrl', 'type', type)
            // verify required parameter 'xAppId' is not null or undefined
            assertParamExists('lsdmxGenerateUrl', 'xAppId', xAppId)
            // verify required parameter 'xAppSignature' is not null or undefined
            assertParamExists('lsdmxGenerateUrl', 'xAppSignature', xAppSignature)
            // verify required parameter 'xAppDate' is not null or undefined
            assertParamExists('lsdmxGenerateUrl', 'xAppDate', xAppDate)
            // verify required parameter 'createUrlRequest' is not null or undefined
            assertParamExists('lsdmxGenerateUrl', 'createUrlRequest', createUrlRequest)
            const localVarPath = `/api/v1/ntes-lsdmx/url`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'POST', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            if (type !== undefined) {
                localVarQueryParameter['type'] = type;
            }

            if (channel !== undefined) {
                localVarQueryParameter['channel'] = channel;
            }



            localVarHeaderParameter['Content-Type'] = 'application/json';

            if (xAppId != null) {
                localVarHeaderParameter['X-App-Id'] = String(xAppId);
            }
            if (xAppSignature != null) {
                localVarHeaderParameter['X-App-Signature'] = String(xAppSignature);
            }
            if (xAppDate != null) {
                localVarHeaderParameter['X-App-Date'] = String(xAppDate);
            }
            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };
            localVarRequestOptions.data = serializeDataIfNeeded(createUrlRequest, localVarRequestOptions, configuration)

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 生成免登 URL
         * @param {string} type 
         * @param {string} ssn 
         * @param {string} roleId 
         * @param {string} xAppId 应用ID
         * @param {string} xAppSignature 应用签名
         * @param {string} xAppDate 应用时间戳
         * @param {string} [channel] 
         * @param {string} [roleName] 
         * @param {string} [hostId] 
         * @param {string} [hostName] 
         * @param {string} [avatar] 
         * @param {string} [level] 
         * @param {string} [createTime] 
         * @param {string} [lastLoginTime] 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        lsdmxGenerateUrlGet: async (type: string, ssn: string, roleId: string, xAppId: string, xAppSignature: string, xAppDate: string, channel?: string, roleName?: string, hostId?: string, hostName?: string, avatar?: string, level?: string, createTime?: string, lastLoginTime?: string, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'type' is not null or undefined
            assertParamExists('lsdmxGenerateUrlGet', 'type', type)
            // verify required parameter 'ssn' is not null or undefined
            assertParamExists('lsdmxGenerateUrlGet', 'ssn', ssn)
            // verify required parameter 'roleId' is not null or undefined
            assertParamExists('lsdmxGenerateUrlGet', 'roleId', roleId)
            // verify required parameter 'xAppId' is not null or undefined
            assertParamExists('lsdmxGenerateUrlGet', 'xAppId', xAppId)
            // verify required parameter 'xAppSignature' is not null or undefined
            assertParamExists('lsdmxGenerateUrlGet', 'xAppSignature', xAppSignature)
            // verify required parameter 'xAppDate' is not null or undefined
            assertParamExists('lsdmxGenerateUrlGet', 'xAppDate', xAppDate)
            const localVarPath = `/api/v1/ntes-lsdmx/url`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            if (type !== undefined) {
                localVarQueryParameter['type'] = type;
            }

            if (channel !== undefined) {
                localVarQueryParameter['channel'] = channel;
            }

            if (ssn !== undefined) {
                localVarQueryParameter['ssn'] = ssn;
            }

            if (roleId !== undefined) {
                localVarQueryParameter['roleId'] = roleId;
            }

            if (roleName !== undefined) {
                localVarQueryParameter['roleName'] = roleName;
            }

            if (hostId !== undefined) {
                localVarQueryParameter['hostId'] = hostId;
            }

            if (hostName !== undefined) {
                localVarQueryParameter['hostName'] = hostName;
            }

            if (avatar !== undefined) {
                localVarQueryParameter['avatar'] = avatar;
            }

            if (level !== undefined) {
                localVarQueryParameter['level'] = level;
            }

            if (createTime !== undefined) {
                localVarQueryParameter['createTime'] = (createTime as any instanceof Date) ?
                    (createTime as any).toISOString() :
                    createTime;
            }

            if (lastLoginTime !== undefined) {
                localVarQueryParameter['lastLoginTime'] = (lastLoginTime as any instanceof Date) ?
                    (lastLoginTime as any).toISOString() :
                    lastLoginTime;
            }



            if (xAppId != null) {
                localVarHeaderParameter['X-App-Id'] = String(xAppId);
            }
            if (xAppSignature != null) {
                localVarHeaderParameter['X-App-Signature'] = String(xAppSignature);
            }
            if (xAppDate != null) {
                localVarHeaderParameter['X-App-Date'] = String(xAppDate);
            }
            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
    }
};

/**
 * LsdmxAuthURLApi - functional programming interface
 * @export
 */
export const LsdmxAuthURLApiFp = function (configuration?: Configuration) {
    const localVarAxiosParamCreator = LsdmxAuthURLApiAxiosParamCreator(configuration)
    return {
        /**
         * 
         * @summary 生成免登 URL
         * @param {string} type 
         * @param {string} xAppId 应用ID
         * @param {string} xAppSignature 应用签名
         * @param {string} xAppDate 应用时间戳
         * @param {CreateUrlRequest} createUrlRequest 
         * @param {string} [channel] 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async lsdmxGenerateUrl(type: string, xAppId: string, xAppSignature: string, xAppDate: string, createUrlRequest: CreateUrlRequest, channel?: string, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<BaseResponseString>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.lsdmxGenerateUrl(type, xAppId, xAppSignature, xAppDate, createUrlRequest, channel, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['LsdmxAuthURLApi.lsdmxGenerateUrl']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 生成免登 URL
         * @param {string} type 
         * @param {string} ssn 
         * @param {string} roleId 
         * @param {string} xAppId 应用ID
         * @param {string} xAppSignature 应用签名
         * @param {string} xAppDate 应用时间戳
         * @param {string} [channel] 
         * @param {string} [roleName] 
         * @param {string} [hostId] 
         * @param {string} [hostName] 
         * @param {string} [avatar] 
         * @param {string} [level] 
         * @param {string} [createTime] 
         * @param {string} [lastLoginTime] 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async lsdmxGenerateUrlGet(type: string, ssn: string, roleId: string, xAppId: string, xAppSignature: string, xAppDate: string, channel?: string, roleName?: string, hostId?: string, hostName?: string, avatar?: string, level?: string, createTime?: string, lastLoginTime?: string, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<BaseResponseString>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.lsdmxGenerateUrlGet(type, ssn, roleId, xAppId, xAppSignature, xAppDate, channel, roleName, hostId, hostName, avatar, level, createTime, lastLoginTime, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['LsdmxAuthURLApi.lsdmxGenerateUrlGet']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
    }
};

/**
 * LsdmxAuthURLApi - factory interface
 * @export
 */
export const LsdmxAuthURLApiFactory = function (configuration?: Configuration, basePath?: string, axios?: AxiosInstance) {
    const localVarFp = LsdmxAuthURLApiFp(configuration)
    return {
        /**
         * 
         * @summary 生成免登 URL
         * @param {LsdmxAuthURLApiLsdmxGenerateUrlRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        lsdmxGenerateUrl(requestParameters: LsdmxAuthURLApiLsdmxGenerateUrlRequest, options?: RawAxiosRequestConfig): AxiosPromise<BaseResponseString> {
            return localVarFp.lsdmxGenerateUrl(requestParameters.type, requestParameters.xAppId, requestParameters.xAppSignature, requestParameters.xAppDate, requestParameters.createUrlRequest, requestParameters.channel, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 生成免登 URL
         * @param {LsdmxAuthURLApiLsdmxGenerateUrlGetRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        lsdmxGenerateUrlGet(requestParameters: LsdmxAuthURLApiLsdmxGenerateUrlGetRequest, options?: RawAxiosRequestConfig): AxiosPromise<BaseResponseString> {
            return localVarFp.lsdmxGenerateUrlGet(requestParameters.type, requestParameters.ssn, requestParameters.roleId, requestParameters.xAppId, requestParameters.xAppSignature, requestParameters.xAppDate, requestParameters.channel, requestParameters.roleName, requestParameters.hostId, requestParameters.hostName, requestParameters.avatar, requestParameters.level, requestParameters.createTime, requestParameters.lastLoginTime, options).then((request) => request(axios, basePath));
        },
    };
};

/**
 * Request parameters for lsdmxGenerateUrl operation in LsdmxAuthURLApi.
 * @export
 * @interface LsdmxAuthURLApiLsdmxGenerateUrlRequest
 */
export interface LsdmxAuthURLApiLsdmxGenerateUrlRequest {
    /**
     * 
     * @type {string}
     * @memberof LsdmxAuthURLApiLsdmxGenerateUrl
     */
    readonly type: string

    /**
     * 应用ID
     * @type {string}
     * @memberof LsdmxAuthURLApiLsdmxGenerateUrl
     */
    readonly xAppId: string

    /**
     * 应用签名
     * @type {string}
     * @memberof LsdmxAuthURLApiLsdmxGenerateUrl
     */
    readonly xAppSignature: string

    /**
     * 应用时间戳
     * @type {string}
     * @memberof LsdmxAuthURLApiLsdmxGenerateUrl
     */
    readonly xAppDate: string

    /**
     * 
     * @type {CreateUrlRequest}
     * @memberof LsdmxAuthURLApiLsdmxGenerateUrl
     */
    readonly createUrlRequest: CreateUrlRequest

    /**
     * 
     * @type {string}
     * @memberof LsdmxAuthURLApiLsdmxGenerateUrl
     */
    readonly channel?: string
}

/**
 * Request parameters for lsdmxGenerateUrlGet operation in LsdmxAuthURLApi.
 * @export
 * @interface LsdmxAuthURLApiLsdmxGenerateUrlGetRequest
 */
export interface LsdmxAuthURLApiLsdmxGenerateUrlGetRequest {
    /**
     * 
     * @type {string}
     * @memberof LsdmxAuthURLApiLsdmxGenerateUrlGet
     */
    readonly type: string

    /**
     * 
     * @type {string}
     * @memberof LsdmxAuthURLApiLsdmxGenerateUrlGet
     */
    readonly ssn: string

    /**
     * 
     * @type {string}
     * @memberof LsdmxAuthURLApiLsdmxGenerateUrlGet
     */
    readonly roleId: string

    /**
     * 应用ID
     * @type {string}
     * @memberof LsdmxAuthURLApiLsdmxGenerateUrlGet
     */
    readonly xAppId: string

    /**
     * 应用签名
     * @type {string}
     * @memberof LsdmxAuthURLApiLsdmxGenerateUrlGet
     */
    readonly xAppSignature: string

    /**
     * 应用时间戳
     * @type {string}
     * @memberof LsdmxAuthURLApiLsdmxGenerateUrlGet
     */
    readonly xAppDate: string

    /**
     * 
     * @type {string}
     * @memberof LsdmxAuthURLApiLsdmxGenerateUrlGet
     */
    readonly channel?: string

    /**
     * 
     * @type {string}
     * @memberof LsdmxAuthURLApiLsdmxGenerateUrlGet
     */
    readonly roleName?: string

    /**
     * 
     * @type {string}
     * @memberof LsdmxAuthURLApiLsdmxGenerateUrlGet
     */
    readonly hostId?: string

    /**
     * 
     * @type {string}
     * @memberof LsdmxAuthURLApiLsdmxGenerateUrlGet
     */
    readonly hostName?: string

    /**
     * 
     * @type {string}
     * @memberof LsdmxAuthURLApiLsdmxGenerateUrlGet
     */
    readonly avatar?: string

    /**
     * 
     * @type {string}
     * @memberof LsdmxAuthURLApiLsdmxGenerateUrlGet
     */
    readonly level?: string

    /**
     * 
     * @type {string}
     * @memberof LsdmxAuthURLApiLsdmxGenerateUrlGet
     */
    readonly createTime?: string

    /**
     * 
     * @type {string}
     * @memberof LsdmxAuthURLApiLsdmxGenerateUrlGet
     */
    readonly lastLoginTime?: string
}

/**
 * LsdmxAuthURLApi - object-oriented interface
 * @export
 * @class LsdmxAuthURLApi
 * @extends {BaseAPI}
 */
export class LsdmxAuthURLApi extends BaseAPI {
    /**
     * 
     * @summary 生成免登 URL
     * @param {LsdmxAuthURLApiLsdmxGenerateUrlRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof LsdmxAuthURLApi
     */
    public lsdmxGenerateUrl(requestParameters: LsdmxAuthURLApiLsdmxGenerateUrlRequest, options?: RawAxiosRequestConfig) {
        return LsdmxAuthURLApiFp(this.configuration).lsdmxGenerateUrl(requestParameters.type, requestParameters.xAppId, requestParameters.xAppSignature, requestParameters.xAppDate, requestParameters.createUrlRequest, requestParameters.channel, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 生成免登 URL
     * @param {LsdmxAuthURLApiLsdmxGenerateUrlGetRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof LsdmxAuthURLApi
     */
    public lsdmxGenerateUrlGet(requestParameters: LsdmxAuthURLApiLsdmxGenerateUrlGetRequest, options?: RawAxiosRequestConfig) {
        return LsdmxAuthURLApiFp(this.configuration).lsdmxGenerateUrlGet(requestParameters.type, requestParameters.ssn, requestParameters.roleId, requestParameters.xAppId, requestParameters.xAppSignature, requestParameters.xAppDate, requestParameters.channel, requestParameters.roleName, requestParameters.hostId, requestParameters.hostName, requestParameters.avatar, requestParameters.level, requestParameters.createTime, requestParameters.lastLoginTime, options).then((request) => request(this.axios, this.basePath));
    }
}



/**
 * NeteaseOpenIDApi - axios parameter creator
 * @export
 */
export const NeteaseOpenIDApiAxiosParamCreator = function (configuration?: Configuration) {
    return {
        /**
         * 
         * @summary 通过 OpenID code 创建访问凭据。
         * @param {string} code 
         * @param {string} redirectUri 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        createUrsToken2: async (code: string, redirectUri: string, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'code' is not null or undefined
            assertParamExists('createUrsToken2', 'code', code)
            // verify required parameter 'redirectUri' is not null or undefined
            assertParamExists('createUrsToken2', 'redirectUri', redirectUri)
            const localVarPath = `/api/v1/ntes-openid/token`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'POST', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            if (code !== undefined) {
                localVarQueryParameter['code'] = code;
            }

            if (redirectUri !== undefined) {
                localVarQueryParameter['redirect_uri'] = redirectUri;
            }



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
    }
};

/**
 * NeteaseOpenIDApi - functional programming interface
 * @export
 */
export const NeteaseOpenIDApiFp = function (configuration?: Configuration) {
    const localVarAxiosParamCreator = NeteaseOpenIDApiAxiosParamCreator(configuration)
    return {
        /**
         * 
         * @summary 通过 OpenID code 创建访问凭据。
         * @param {string} code 
         * @param {string} redirectUri 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async createUrsToken2(code: string, redirectUri: string, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<string>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.createUrsToken2(code, redirectUri, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['NeteaseOpenIDApi.createUrsToken2']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
    }
};

/**
 * NeteaseOpenIDApi - factory interface
 * @export
 */
export const NeteaseOpenIDApiFactory = function (configuration?: Configuration, basePath?: string, axios?: AxiosInstance) {
    const localVarFp = NeteaseOpenIDApiFp(configuration)
    return {
        /**
         * 
         * @summary 通过 OpenID code 创建访问凭据。
         * @param {NeteaseOpenIDApiCreateUrsToken2Request} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        createUrsToken2(requestParameters: NeteaseOpenIDApiCreateUrsToken2Request, options?: RawAxiosRequestConfig): AxiosPromise<string> {
            return localVarFp.createUrsToken2(requestParameters.code, requestParameters.redirectUri, options).then((request) => request(axios, basePath));
        },
    };
};

/**
 * Request parameters for createUrsToken2 operation in NeteaseOpenIDApi.
 * @export
 * @interface NeteaseOpenIDApiCreateUrsToken2Request
 */
export interface NeteaseOpenIDApiCreateUrsToken2Request {
    /**
     * 
     * @type {string}
     * @memberof NeteaseOpenIDApiCreateUrsToken2
     */
    readonly code: string

    /**
     * 
     * @type {string}
     * @memberof NeteaseOpenIDApiCreateUrsToken2
     */
    readonly redirectUri: string
}

/**
 * NeteaseOpenIDApi - object-oriented interface
 * @export
 * @class NeteaseOpenIDApi
 * @extends {BaseAPI}
 */
export class NeteaseOpenIDApi extends BaseAPI {
    /**
     * 
     * @summary 通过 OpenID code 创建访问凭据。
     * @param {NeteaseOpenIDApiCreateUrsToken2Request} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof NeteaseOpenIDApi
     */
    public createUrsToken2(requestParameters: NeteaseOpenIDApiCreateUrsToken2Request, options?: RawAxiosRequestConfig) {
        return NeteaseOpenIDApiFp(this.configuration).createUrsToken2(requestParameters.code, requestParameters.redirectUri, options).then((request) => request(this.axios, this.basePath));
    }
}



/**
 * PostAdminApi - axios parameter creator
 * @export
 */
export const PostAdminApiAxiosParamCreator = function (configuration?: Configuration) {
    return {
        /**
         * 
         * @summary 新增帖子
         * @param {PostCreateRequest} postCreateRequest 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        createPostAdmin: async (postCreateRequest: PostCreateRequest, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'postCreateRequest' is not null or undefined
            assertParamExists('createPostAdmin', 'postCreateRequest', postCreateRequest)
            const localVarPath = `/api/v1/admin/post`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'POST', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            localVarHeaderParameter['Content-Type'] = 'application/json';

            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };
            localVarRequestOptions.data = serializeDataIfNeeded(postCreateRequest, localVarRequestOptions, configuration)

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 根据id删除帖子
         * @param {string} id 帖子id
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        deletePostById: async (id: string, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'id' is not null or undefined
            assertParamExists('deletePostById', 'id', id)
            const localVarPath = `/api/v1/admin/post/{id}`
                .replace(`{${"id"}}`, encodeURIComponent(String(id)));
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'DELETE', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 根据id查询帖子
         * @param {string} id 帖子id
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getPostByIdAdmin: async (id: string, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'id' is not null or undefined
            assertParamExists('getPostByIdAdmin', 'id', id)
            const localVarPath = `/api/v1/admin/post/{id}`
                .replace(`{${"id"}}`, encodeURIComponent(String(id)));
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 分页查询帖子列表
         * @param {number} page 页码，从1开始
         * @param {number} size 每页大小
         * @param {string} [keyword] 关键字
         * @param {string} [level1TagId] 一级标签id
         * @param {string} [level2TagId] 二级标签id
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        pagePostAdmin: async (page: number, size: number, keyword?: string, level1TagId?: string, level2TagId?: string, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'page' is not null or undefined
            assertParamExists('pagePostAdmin', 'page', page)
            // verify required parameter 'size' is not null or undefined
            assertParamExists('pagePostAdmin', 'size', size)
            const localVarPath = `/api/v1/admin/post/page`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)

            if (keyword !== undefined) {
                localVarQueryParameter['keyword'] = keyword;
            }

            if (level1TagId !== undefined) {
                localVarQueryParameter['level1TagId'] = level1TagId;
            }

            if (level2TagId !== undefined) {
                localVarQueryParameter['level2TagId'] = level2TagId;
            }

            if (page !== undefined) {
                localVarQueryParameter['page'] = page;
            }

            if (size !== undefined) {
                localVarQueryParameter['size'] = size;
            }



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 查询帖子统计数据
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        postStatisticsAdmin: async (options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            const localVarPath = `/api/v1/admin/post/statistics`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 更新帖子
         * @param {string} id 帖子id
         * @param {PostUpdateRequest} postUpdateRequest 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        updatePostAdmin: async (id: string, postUpdateRequest: PostUpdateRequest, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'id' is not null or undefined
            assertParamExists('updatePostAdmin', 'id', id)
            // verify required parameter 'postUpdateRequest' is not null or undefined
            assertParamExists('updatePostAdmin', 'postUpdateRequest', postUpdateRequest)
            const localVarPath = `/api/v1/admin/post/{id}`
                .replace(`{${"id"}}`, encodeURIComponent(String(id)));
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'PUT', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            localVarHeaderParameter['Content-Type'] = 'application/json';

            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };
            localVarRequestOptions.data = serializeDataIfNeeded(postUpdateRequest, localVarRequestOptions, configuration)

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 更新帖子虚假数据
         * @param {string} id 帖子id
         * @param {PostDisplayCountsUpdateRequest} postDisplayCountsUpdateRequest 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        updatePostDisplayCountsAdmin: async (id: string, postDisplayCountsUpdateRequest: PostDisplayCountsUpdateRequest, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'id' is not null or undefined
            assertParamExists('updatePostDisplayCountsAdmin', 'id', id)
            // verify required parameter 'postDisplayCountsUpdateRequest' is not null or undefined
            assertParamExists('updatePostDisplayCountsAdmin', 'postDisplayCountsUpdateRequest', postDisplayCountsUpdateRequest)
            const localVarPath = `/api/v1/admin/post/{id}/display-counts`
                .replace(`{${"id"}}`, encodeURIComponent(String(id)));
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'PUT', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            localVarHeaderParameter['Content-Type'] = 'application/json';

            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };
            localVarRequestOptions.data = serializeDataIfNeeded(postDisplayCountsUpdateRequest, localVarRequestOptions, configuration)

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 更新帖子可见性
         * @param {string} id 帖子id
         * @param {PostVisibleUpdateRequest} postVisibleUpdateRequest 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        updatePostVisibleAdmin: async (id: string, postVisibleUpdateRequest: PostVisibleUpdateRequest, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'id' is not null or undefined
            assertParamExists('updatePostVisibleAdmin', 'id', id)
            // verify required parameter 'postVisibleUpdateRequest' is not null or undefined
            assertParamExists('updatePostVisibleAdmin', 'postVisibleUpdateRequest', postVisibleUpdateRequest)
            const localVarPath = `/api/v1/admin/post/{id}/visible`
                .replace(`{${"id"}}`, encodeURIComponent(String(id)));
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'PUT', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            localVarHeaderParameter['Content-Type'] = 'application/json';

            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };
            localVarRequestOptions.data = serializeDataIfNeeded(postVisibleUpdateRequest, localVarRequestOptions, configuration)

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
    }
};

/**
 * PostAdminApi - functional programming interface
 * @export
 */
export const PostAdminApiFp = function (configuration?: Configuration) {
    const localVarAxiosParamCreator = PostAdminApiAxiosParamCreator(configuration)
    return {
        /**
         * 
         * @summary 新增帖子
         * @param {PostCreateRequest} postCreateRequest 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async createPostAdmin(postCreateRequest: PostCreateRequest, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<Post>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.createPostAdmin(postCreateRequest, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['PostAdminApi.createPostAdmin']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 根据id删除帖子
         * @param {string} id 帖子id
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async deletePostById(id: string, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<boolean>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.deletePostById(id, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['PostAdminApi.deletePostById']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 根据id查询帖子
         * @param {string} id 帖子id
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async getPostByIdAdmin(id: string, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<Post>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.getPostByIdAdmin(id, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['PostAdminApi.getPostByIdAdmin']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 分页查询帖子列表
         * @param {number} page 页码，从1开始
         * @param {number} size 每页大小
         * @param {string} [keyword] 关键字
         * @param {string} [level1TagId] 一级标签id
         * @param {string} [level2TagId] 二级标签id
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async pagePostAdmin(page: number, size: number, keyword?: string, level1TagId?: string, level2TagId?: string, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<PagePost>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.pagePostAdmin(page, size, keyword, level1TagId, level2TagId, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['PostAdminApi.pagePostAdmin']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 查询帖子统计数据
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async postStatisticsAdmin(options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<PostStatisticsVO>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.postStatisticsAdmin(options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['PostAdminApi.postStatisticsAdmin']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 更新帖子
         * @param {string} id 帖子id
         * @param {PostUpdateRequest} postUpdateRequest 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async updatePostAdmin(id: string, postUpdateRequest: PostUpdateRequest, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<boolean>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.updatePostAdmin(id, postUpdateRequest, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['PostAdminApi.updatePostAdmin']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 更新帖子虚假数据
         * @param {string} id 帖子id
         * @param {PostDisplayCountsUpdateRequest} postDisplayCountsUpdateRequest 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async updatePostDisplayCountsAdmin(id: string, postDisplayCountsUpdateRequest: PostDisplayCountsUpdateRequest, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<boolean>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.updatePostDisplayCountsAdmin(id, postDisplayCountsUpdateRequest, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['PostAdminApi.updatePostDisplayCountsAdmin']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 更新帖子可见性
         * @param {string} id 帖子id
         * @param {PostVisibleUpdateRequest} postVisibleUpdateRequest 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async updatePostVisibleAdmin(id: string, postVisibleUpdateRequest: PostVisibleUpdateRequest, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<boolean>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.updatePostVisibleAdmin(id, postVisibleUpdateRequest, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['PostAdminApi.updatePostVisibleAdmin']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
    }
};

/**
 * PostAdminApi - factory interface
 * @export
 */
export const PostAdminApiFactory = function (configuration?: Configuration, basePath?: string, axios?: AxiosInstance) {
    const localVarFp = PostAdminApiFp(configuration)
    return {
        /**
         * 
         * @summary 新增帖子
         * @param {PostAdminApiCreatePostAdminRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        createPostAdmin(requestParameters: PostAdminApiCreatePostAdminRequest, options?: RawAxiosRequestConfig): AxiosPromise<Post> {
            return localVarFp.createPostAdmin(requestParameters.postCreateRequest, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 根据id删除帖子
         * @param {PostAdminApiDeletePostByIdRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        deletePostById(requestParameters: PostAdminApiDeletePostByIdRequest, options?: RawAxiosRequestConfig): AxiosPromise<boolean> {
            return localVarFp.deletePostById(requestParameters.id, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 根据id查询帖子
         * @param {PostAdminApiGetPostByIdAdminRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getPostByIdAdmin(requestParameters: PostAdminApiGetPostByIdAdminRequest, options?: RawAxiosRequestConfig): AxiosPromise<Post> {
            return localVarFp.getPostByIdAdmin(requestParameters.id, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 分页查询帖子列表
         * @param {PostAdminApiPagePostAdminRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        pagePostAdmin(requestParameters: PostAdminApiPagePostAdminRequest, options?: RawAxiosRequestConfig): AxiosPromise<PagePost> {
            return localVarFp.pagePostAdmin(requestParameters.page, requestParameters.size, requestParameters.keyword, requestParameters.level1TagId, requestParameters.level2TagId, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 查询帖子统计数据
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        postStatisticsAdmin(options?: RawAxiosRequestConfig): AxiosPromise<PostStatisticsVO> {
            return localVarFp.postStatisticsAdmin(options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 更新帖子
         * @param {PostAdminApiUpdatePostAdminRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        updatePostAdmin(requestParameters: PostAdminApiUpdatePostAdminRequest, options?: RawAxiosRequestConfig): AxiosPromise<boolean> {
            return localVarFp.updatePostAdmin(requestParameters.id, requestParameters.postUpdateRequest, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 更新帖子虚假数据
         * @param {PostAdminApiUpdatePostDisplayCountsAdminRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        updatePostDisplayCountsAdmin(requestParameters: PostAdminApiUpdatePostDisplayCountsAdminRequest, options?: RawAxiosRequestConfig): AxiosPromise<boolean> {
            return localVarFp.updatePostDisplayCountsAdmin(requestParameters.id, requestParameters.postDisplayCountsUpdateRequest, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 更新帖子可见性
         * @param {PostAdminApiUpdatePostVisibleAdminRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        updatePostVisibleAdmin(requestParameters: PostAdminApiUpdatePostVisibleAdminRequest, options?: RawAxiosRequestConfig): AxiosPromise<boolean> {
            return localVarFp.updatePostVisibleAdmin(requestParameters.id, requestParameters.postVisibleUpdateRequest, options).then((request) => request(axios, basePath));
        },
    };
};

/**
 * Request parameters for createPostAdmin operation in PostAdminApi.
 * @export
 * @interface PostAdminApiCreatePostAdminRequest
 */
export interface PostAdminApiCreatePostAdminRequest {
    /**
     * 
     * @type {PostCreateRequest}
     * @memberof PostAdminApiCreatePostAdmin
     */
    readonly postCreateRequest: PostCreateRequest
}

/**
 * Request parameters for deletePostById operation in PostAdminApi.
 * @export
 * @interface PostAdminApiDeletePostByIdRequest
 */
export interface PostAdminApiDeletePostByIdRequest {
    /**
     * 帖子id
     * @type {string}
     * @memberof PostAdminApiDeletePostById
     */
    readonly id: string
}

/**
 * Request parameters for getPostByIdAdmin operation in PostAdminApi.
 * @export
 * @interface PostAdminApiGetPostByIdAdminRequest
 */
export interface PostAdminApiGetPostByIdAdminRequest {
    /**
     * 帖子id
     * @type {string}
     * @memberof PostAdminApiGetPostByIdAdmin
     */
    readonly id: string
}

/**
 * Request parameters for pagePostAdmin operation in PostAdminApi.
 * @export
 * @interface PostAdminApiPagePostAdminRequest
 */
export interface PostAdminApiPagePostAdminRequest {
    /**
     * 页码，从1开始
     * @type {number}
     * @memberof PostAdminApiPagePostAdmin
     */
    readonly page: number

    /**
     * 每页大小
     * @type {number}
     * @memberof PostAdminApiPagePostAdmin
     */
    readonly size: number

    /**
     * 关键字
     * @type {string}
     * @memberof PostAdminApiPagePostAdmin
     */
    readonly keyword?: string

    /**
     * 一级标签id
     * @type {string}
     * @memberof PostAdminApiPagePostAdmin
     */
    readonly level1TagId?: string

    /**
     * 二级标签id
     * @type {string}
     * @memberof PostAdminApiPagePostAdmin
     */
    readonly level2TagId?: string
}

/**
 * Request parameters for updatePostAdmin operation in PostAdminApi.
 * @export
 * @interface PostAdminApiUpdatePostAdminRequest
 */
export interface PostAdminApiUpdatePostAdminRequest {
    /**
     * 帖子id
     * @type {string}
     * @memberof PostAdminApiUpdatePostAdmin
     */
    readonly id: string

    /**
     * 
     * @type {PostUpdateRequest}
     * @memberof PostAdminApiUpdatePostAdmin
     */
    readonly postUpdateRequest: PostUpdateRequest
}

/**
 * Request parameters for updatePostDisplayCountsAdmin operation in PostAdminApi.
 * @export
 * @interface PostAdminApiUpdatePostDisplayCountsAdminRequest
 */
export interface PostAdminApiUpdatePostDisplayCountsAdminRequest {
    /**
     * 帖子id
     * @type {string}
     * @memberof PostAdminApiUpdatePostDisplayCountsAdmin
     */
    readonly id: string

    /**
     * 
     * @type {PostDisplayCountsUpdateRequest}
     * @memberof PostAdminApiUpdatePostDisplayCountsAdmin
     */
    readonly postDisplayCountsUpdateRequest: PostDisplayCountsUpdateRequest
}

/**
 * Request parameters for updatePostVisibleAdmin operation in PostAdminApi.
 * @export
 * @interface PostAdminApiUpdatePostVisibleAdminRequest
 */
export interface PostAdminApiUpdatePostVisibleAdminRequest {
    /**
     * 帖子id
     * @type {string}
     * @memberof PostAdminApiUpdatePostVisibleAdmin
     */
    readonly id: string

    /**
     * 
     * @type {PostVisibleUpdateRequest}
     * @memberof PostAdminApiUpdatePostVisibleAdmin
     */
    readonly postVisibleUpdateRequest: PostVisibleUpdateRequest
}

/**
 * PostAdminApi - object-oriented interface
 * @export
 * @class PostAdminApi
 * @extends {BaseAPI}
 */
export class PostAdminApi extends BaseAPI {
    /**
     * 
     * @summary 新增帖子
     * @param {PostAdminApiCreatePostAdminRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof PostAdminApi
     */
    public createPostAdmin(requestParameters: PostAdminApiCreatePostAdminRequest, options?: RawAxiosRequestConfig) {
        return PostAdminApiFp(this.configuration).createPostAdmin(requestParameters.postCreateRequest, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 根据id删除帖子
     * @param {PostAdminApiDeletePostByIdRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof PostAdminApi
     */
    public deletePostById(requestParameters: PostAdminApiDeletePostByIdRequest, options?: RawAxiosRequestConfig) {
        return PostAdminApiFp(this.configuration).deletePostById(requestParameters.id, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 根据id查询帖子
     * @param {PostAdminApiGetPostByIdAdminRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof PostAdminApi
     */
    public getPostByIdAdmin(requestParameters: PostAdminApiGetPostByIdAdminRequest, options?: RawAxiosRequestConfig) {
        return PostAdminApiFp(this.configuration).getPostByIdAdmin(requestParameters.id, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 分页查询帖子列表
     * @param {PostAdminApiPagePostAdminRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof PostAdminApi
     */
    public pagePostAdmin(requestParameters: PostAdminApiPagePostAdminRequest, options?: RawAxiosRequestConfig) {
        return PostAdminApiFp(this.configuration).pagePostAdmin(requestParameters.page, requestParameters.size, requestParameters.keyword, requestParameters.level1TagId, requestParameters.level2TagId, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 查询帖子统计数据
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof PostAdminApi
     */
    public postStatisticsAdmin(options?: RawAxiosRequestConfig) {
        return PostAdminApiFp(this.configuration).postStatisticsAdmin(options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 更新帖子
     * @param {PostAdminApiUpdatePostAdminRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof PostAdminApi
     */
    public updatePostAdmin(requestParameters: PostAdminApiUpdatePostAdminRequest, options?: RawAxiosRequestConfig) {
        return PostAdminApiFp(this.configuration).updatePostAdmin(requestParameters.id, requestParameters.postUpdateRequest, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 更新帖子虚假数据
     * @param {PostAdminApiUpdatePostDisplayCountsAdminRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof PostAdminApi
     */
    public updatePostDisplayCountsAdmin(requestParameters: PostAdminApiUpdatePostDisplayCountsAdminRequest, options?: RawAxiosRequestConfig) {
        return PostAdminApiFp(this.configuration).updatePostDisplayCountsAdmin(requestParameters.id, requestParameters.postDisplayCountsUpdateRequest, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 更新帖子可见性
     * @param {PostAdminApiUpdatePostVisibleAdminRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof PostAdminApi
     */
    public updatePostVisibleAdmin(requestParameters: PostAdminApiUpdatePostVisibleAdminRequest, options?: RawAxiosRequestConfig) {
        return PostAdminApiFp(this.configuration).updatePostVisibleAdmin(requestParameters.id, requestParameters.postVisibleUpdateRequest, options).then((request) => request(this.axios, this.basePath));
    }
}



/**
 * PostAuthorAdminApi - axios parameter creator
 * @export
 */
export const PostAuthorAdminApiAxiosParamCreator = function (configuration?: Configuration) {
    return {
        /**
         * 
         * @summary 新增帖子作者
         * @param {PostAuthorSaveRequest} postAuthorSaveRequest 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        createPostAuthorAdmin: async (postAuthorSaveRequest: PostAuthorSaveRequest, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'postAuthorSaveRequest' is not null or undefined
            assertParamExists('createPostAuthorAdmin', 'postAuthorSaveRequest', postAuthorSaveRequest)
            const localVarPath = `/api/v1/admin/post-author`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'POST', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            localVarHeaderParameter['Content-Type'] = 'application/json';

            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };
            localVarRequestOptions.data = serializeDataIfNeeded(postAuthorSaveRequest, localVarRequestOptions, configuration)

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 根据id删除帖子作者
         * @param {string} id 作者id
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        deletePostAuthorByIdAdmin: async (id: string, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'id' is not null or undefined
            assertParamExists('deletePostAuthorByIdAdmin', 'id', id)
            const localVarPath = `/api/v1/admin/post-author/{id}`
                .replace(`{${"id"}}`, encodeURIComponent(String(id)));
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'DELETE', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 根据id查询帖子作者
         * @param {string} id 作者id
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getPostAuthorByIdAdmin: async (id: string, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'id' is not null or undefined
            assertParamExists('getPostAuthorByIdAdmin', 'id', id)
            const localVarPath = `/api/v1/admin/post-author/{id}`
                .replace(`{${"id"}}`, encodeURIComponent(String(id)));
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 查询帖子作者列表
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        listPostAuthorAdmin: async (options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            const localVarPath = `/api/v1/admin/post-author/list`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 修改帖子作者
         * @param {string} id 作者id
         * @param {PostAuthorSaveRequest} postAuthorSaveRequest 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        updatePostAuthorAdmin: async (id: string, postAuthorSaveRequest: PostAuthorSaveRequest, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'id' is not null or undefined
            assertParamExists('updatePostAuthorAdmin', 'id', id)
            // verify required parameter 'postAuthorSaveRequest' is not null or undefined
            assertParamExists('updatePostAuthorAdmin', 'postAuthorSaveRequest', postAuthorSaveRequest)
            const localVarPath = `/api/v1/admin/post-author/{id}`
                .replace(`{${"id"}}`, encodeURIComponent(String(id)));
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'PUT', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            localVarHeaderParameter['Content-Type'] = 'application/json';

            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };
            localVarRequestOptions.data = serializeDataIfNeeded(postAuthorSaveRequest, localVarRequestOptions, configuration)

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
    }
};

/**
 * PostAuthorAdminApi - functional programming interface
 * @export
 */
export const PostAuthorAdminApiFp = function (configuration?: Configuration) {
    const localVarAxiosParamCreator = PostAuthorAdminApiAxiosParamCreator(configuration)
    return {
        /**
         * 
         * @summary 新增帖子作者
         * @param {PostAuthorSaveRequest} postAuthorSaveRequest 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async createPostAuthorAdmin(postAuthorSaveRequest: PostAuthorSaveRequest, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<PostAuthor>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.createPostAuthorAdmin(postAuthorSaveRequest, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['PostAuthorAdminApi.createPostAuthorAdmin']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 根据id删除帖子作者
         * @param {string} id 作者id
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async deletePostAuthorByIdAdmin(id: string, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<boolean>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.deletePostAuthorByIdAdmin(id, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['PostAuthorAdminApi.deletePostAuthorByIdAdmin']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 根据id查询帖子作者
         * @param {string} id 作者id
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async getPostAuthorByIdAdmin(id: string, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<PostAuthor>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.getPostAuthorByIdAdmin(id, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['PostAuthorAdminApi.getPostAuthorByIdAdmin']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 查询帖子作者列表
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async listPostAuthorAdmin(options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<Array<PostAuthor>>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.listPostAuthorAdmin(options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['PostAuthorAdminApi.listPostAuthorAdmin']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 修改帖子作者
         * @param {string} id 作者id
         * @param {PostAuthorSaveRequest} postAuthorSaveRequest 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async updatePostAuthorAdmin(id: string, postAuthorSaveRequest: PostAuthorSaveRequest, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<boolean>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.updatePostAuthorAdmin(id, postAuthorSaveRequest, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['PostAuthorAdminApi.updatePostAuthorAdmin']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
    }
};

/**
 * PostAuthorAdminApi - factory interface
 * @export
 */
export const PostAuthorAdminApiFactory = function (configuration?: Configuration, basePath?: string, axios?: AxiosInstance) {
    const localVarFp = PostAuthorAdminApiFp(configuration)
    return {
        /**
         * 
         * @summary 新增帖子作者
         * @param {PostAuthorAdminApiCreatePostAuthorAdminRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        createPostAuthorAdmin(requestParameters: PostAuthorAdminApiCreatePostAuthorAdminRequest, options?: RawAxiosRequestConfig): AxiosPromise<PostAuthor> {
            return localVarFp.createPostAuthorAdmin(requestParameters.postAuthorSaveRequest, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 根据id删除帖子作者
         * @param {PostAuthorAdminApiDeletePostAuthorByIdAdminRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        deletePostAuthorByIdAdmin(requestParameters: PostAuthorAdminApiDeletePostAuthorByIdAdminRequest, options?: RawAxiosRequestConfig): AxiosPromise<boolean> {
            return localVarFp.deletePostAuthorByIdAdmin(requestParameters.id, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 根据id查询帖子作者
         * @param {PostAuthorAdminApiGetPostAuthorByIdAdminRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getPostAuthorByIdAdmin(requestParameters: PostAuthorAdminApiGetPostAuthorByIdAdminRequest, options?: RawAxiosRequestConfig): AxiosPromise<PostAuthor> {
            return localVarFp.getPostAuthorByIdAdmin(requestParameters.id, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 查询帖子作者列表
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        listPostAuthorAdmin(options?: RawAxiosRequestConfig): AxiosPromise<Array<PostAuthor>> {
            return localVarFp.listPostAuthorAdmin(options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 修改帖子作者
         * @param {PostAuthorAdminApiUpdatePostAuthorAdminRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        updatePostAuthorAdmin(requestParameters: PostAuthorAdminApiUpdatePostAuthorAdminRequest, options?: RawAxiosRequestConfig): AxiosPromise<boolean> {
            return localVarFp.updatePostAuthorAdmin(requestParameters.id, requestParameters.postAuthorSaveRequest, options).then((request) => request(axios, basePath));
        },
    };
};

/**
 * Request parameters for createPostAuthorAdmin operation in PostAuthorAdminApi.
 * @export
 * @interface PostAuthorAdminApiCreatePostAuthorAdminRequest
 */
export interface PostAuthorAdminApiCreatePostAuthorAdminRequest {
    /**
     * 
     * @type {PostAuthorSaveRequest}
     * @memberof PostAuthorAdminApiCreatePostAuthorAdmin
     */
    readonly postAuthorSaveRequest: PostAuthorSaveRequest
}

/**
 * Request parameters for deletePostAuthorByIdAdmin operation in PostAuthorAdminApi.
 * @export
 * @interface PostAuthorAdminApiDeletePostAuthorByIdAdminRequest
 */
export interface PostAuthorAdminApiDeletePostAuthorByIdAdminRequest {
    /**
     * 作者id
     * @type {string}
     * @memberof PostAuthorAdminApiDeletePostAuthorByIdAdmin
     */
    readonly id: string
}

/**
 * Request parameters for getPostAuthorByIdAdmin operation in PostAuthorAdminApi.
 * @export
 * @interface PostAuthorAdminApiGetPostAuthorByIdAdminRequest
 */
export interface PostAuthorAdminApiGetPostAuthorByIdAdminRequest {
    /**
     * 作者id
     * @type {string}
     * @memberof PostAuthorAdminApiGetPostAuthorByIdAdmin
     */
    readonly id: string
}

/**
 * Request parameters for updatePostAuthorAdmin operation in PostAuthorAdminApi.
 * @export
 * @interface PostAuthorAdminApiUpdatePostAuthorAdminRequest
 */
export interface PostAuthorAdminApiUpdatePostAuthorAdminRequest {
    /**
     * 作者id
     * @type {string}
     * @memberof PostAuthorAdminApiUpdatePostAuthorAdmin
     */
    readonly id: string

    /**
     * 
     * @type {PostAuthorSaveRequest}
     * @memberof PostAuthorAdminApiUpdatePostAuthorAdmin
     */
    readonly postAuthorSaveRequest: PostAuthorSaveRequest
}

/**
 * PostAuthorAdminApi - object-oriented interface
 * @export
 * @class PostAuthorAdminApi
 * @extends {BaseAPI}
 */
export class PostAuthorAdminApi extends BaseAPI {
    /**
     * 
     * @summary 新增帖子作者
     * @param {PostAuthorAdminApiCreatePostAuthorAdminRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof PostAuthorAdminApi
     */
    public createPostAuthorAdmin(requestParameters: PostAuthorAdminApiCreatePostAuthorAdminRequest, options?: RawAxiosRequestConfig) {
        return PostAuthorAdminApiFp(this.configuration).createPostAuthorAdmin(requestParameters.postAuthorSaveRequest, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 根据id删除帖子作者
     * @param {PostAuthorAdminApiDeletePostAuthorByIdAdminRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof PostAuthorAdminApi
     */
    public deletePostAuthorByIdAdmin(requestParameters: PostAuthorAdminApiDeletePostAuthorByIdAdminRequest, options?: RawAxiosRequestConfig) {
        return PostAuthorAdminApiFp(this.configuration).deletePostAuthorByIdAdmin(requestParameters.id, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 根据id查询帖子作者
     * @param {PostAuthorAdminApiGetPostAuthorByIdAdminRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof PostAuthorAdminApi
     */
    public getPostAuthorByIdAdmin(requestParameters: PostAuthorAdminApiGetPostAuthorByIdAdminRequest, options?: RawAxiosRequestConfig) {
        return PostAuthorAdminApiFp(this.configuration).getPostAuthorByIdAdmin(requestParameters.id, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 查询帖子作者列表
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof PostAuthorAdminApi
     */
    public listPostAuthorAdmin(options?: RawAxiosRequestConfig) {
        return PostAuthorAdminApiFp(this.configuration).listPostAuthorAdmin(options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 修改帖子作者
     * @param {PostAuthorAdminApiUpdatePostAuthorAdminRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof PostAuthorAdminApi
     */
    public updatePostAuthorAdmin(requestParameters: PostAuthorAdminApiUpdatePostAuthorAdminRequest, options?: RawAxiosRequestConfig) {
        return PostAuthorAdminApiFp(this.configuration).updatePostAuthorAdmin(requestParameters.id, requestParameters.postAuthorSaveRequest, options).then((request) => request(this.axios, this.basePath));
    }
}



/**
 * PostAuthorMpApi - axios parameter creator
 * @export
 */
export const PostAuthorMpApiAxiosParamCreator = function (configuration?: Configuration) {
    return {
        /**
         * 
         * @summary 根据id查询帖子作者
         * @param {string} id 作者id
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getPostAuthorByIdMp: async (id: string, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'id' is not null or undefined
            assertParamExists('getPostAuthorByIdMp', 'id', id)
            const localVarPath = `/api/v1/mp/post-author/{id}`
                .replace(`{${"id"}}`, encodeURIComponent(String(id)));
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
    }
};

/**
 * PostAuthorMpApi - functional programming interface
 * @export
 */
export const PostAuthorMpApiFp = function (configuration?: Configuration) {
    const localVarAxiosParamCreator = PostAuthorMpApiAxiosParamCreator(configuration)
    return {
        /**
         * 
         * @summary 根据id查询帖子作者
         * @param {string} id 作者id
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async getPostAuthorByIdMp(id: string, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<PostAuthor>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.getPostAuthorByIdMp(id, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['PostAuthorMpApi.getPostAuthorByIdMp']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
    }
};

/**
 * PostAuthorMpApi - factory interface
 * @export
 */
export const PostAuthorMpApiFactory = function (configuration?: Configuration, basePath?: string, axios?: AxiosInstance) {
    const localVarFp = PostAuthorMpApiFp(configuration)
    return {
        /**
         * 
         * @summary 根据id查询帖子作者
         * @param {PostAuthorMpApiGetPostAuthorByIdMpRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getPostAuthorByIdMp(requestParameters: PostAuthorMpApiGetPostAuthorByIdMpRequest, options?: RawAxiosRequestConfig): AxiosPromise<PostAuthor> {
            return localVarFp.getPostAuthorByIdMp(requestParameters.id, options).then((request) => request(axios, basePath));
        },
    };
};

/**
 * Request parameters for getPostAuthorByIdMp operation in PostAuthorMpApi.
 * @export
 * @interface PostAuthorMpApiGetPostAuthorByIdMpRequest
 */
export interface PostAuthorMpApiGetPostAuthorByIdMpRequest {
    /**
     * 作者id
     * @type {string}
     * @memberof PostAuthorMpApiGetPostAuthorByIdMp
     */
    readonly id: string
}

/**
 * PostAuthorMpApi - object-oriented interface
 * @export
 * @class PostAuthorMpApi
 * @extends {BaseAPI}
 */
export class PostAuthorMpApi extends BaseAPI {
    /**
     * 
     * @summary 根据id查询帖子作者
     * @param {PostAuthorMpApiGetPostAuthorByIdMpRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof PostAuthorMpApi
     */
    public getPostAuthorByIdMp(requestParameters: PostAuthorMpApiGetPostAuthorByIdMpRequest, options?: RawAxiosRequestConfig) {
        return PostAuthorMpApiFp(this.configuration).getPostAuthorByIdMp(requestParameters.id, options).then((request) => request(this.axios, this.basePath));
    }
}



/**
 * PostMpApi - axios parameter creator
 * @export
 */
export const PostMpApiAxiosParamCreator = function (configuration?: Configuration) {
    return {
        /**
         * 
         * @summary 前台根据id查询帖子
         * @param {string} id 帖子id
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getPostByIdMp: async (id: string, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'id' is not null or undefined
            assertParamExists('getPostByIdMp', 'id', id)
            const localVarPath = `/api/v1/mp/post/{id}`
                .replace(`{${"id"}}`, encodeURIComponent(String(id)));
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 帖子转发，增加帖子转发量
         * @param {string} id 帖子id
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        incrementPostForwardCountMp: async (id: string, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'id' is not null or undefined
            assertParamExists('incrementPostForwardCountMp', 'id', id)
            const localVarPath = `/api/v1/mp/post/{id}/forward`
                .replace(`{${"id"}}`, encodeURIComponent(String(id)));
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'PUT', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 增加帖子浏览量
         * @param {string} id 帖子id
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        incrementPostViewCountMp: async (id: string, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'id' is not null or undefined
            assertParamExists('incrementPostViewCountMp', 'id', id)
            const localVarPath = `/api/v1/mp/post/{id}/view`
                .replace(`{${"id"}}`, encodeURIComponent(String(id)));
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'PUT', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 前台分页查询帖子列表
         * @param {number} page 页码，从1开始
         * @param {number} size 每页大小
         * @param {string} [keyword] 关键字
         * @param {string} [level1TagId] 一级标签id
         * @param {string} [level2TagId] 二级标签id
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        pagePostMp: async (page: number, size: number, keyword?: string, level1TagId?: string, level2TagId?: string, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'page' is not null or undefined
            assertParamExists('pagePostMp', 'page', page)
            // verify required parameter 'size' is not null or undefined
            assertParamExists('pagePostMp', 'size', size)
            const localVarPath = `/api/v1/mp/post/page`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)

            if (keyword !== undefined) {
                localVarQueryParameter['keyword'] = keyword;
            }

            if (level1TagId !== undefined) {
                localVarQueryParameter['level1TagId'] = level1TagId;
            }

            if (level2TagId !== undefined) {
                localVarQueryParameter['level2TagId'] = level2TagId;
            }

            if (page !== undefined) {
                localVarQueryParameter['page'] = page;
            }

            if (size !== undefined) {
                localVarQueryParameter['size'] = size;
            }



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
    }
};

/**
 * PostMpApi - functional programming interface
 * @export
 */
export const PostMpApiFp = function (configuration?: Configuration) {
    const localVarAxiosParamCreator = PostMpApiAxiosParamCreator(configuration)
    return {
        /**
         * 
         * @summary 前台根据id查询帖子
         * @param {string} id 帖子id
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async getPostByIdMp(id: string, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<Post>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.getPostByIdMp(id, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['PostMpApi.getPostByIdMp']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 帖子转发，增加帖子转发量
         * @param {string} id 帖子id
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async incrementPostForwardCountMp(id: string, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<boolean>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.incrementPostForwardCountMp(id, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['PostMpApi.incrementPostForwardCountMp']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 增加帖子浏览量
         * @param {string} id 帖子id
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async incrementPostViewCountMp(id: string, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<boolean>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.incrementPostViewCountMp(id, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['PostMpApi.incrementPostViewCountMp']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 前台分页查询帖子列表
         * @param {number} page 页码，从1开始
         * @param {number} size 每页大小
         * @param {string} [keyword] 关键字
         * @param {string} [level1TagId] 一级标签id
         * @param {string} [level2TagId] 二级标签id
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async pagePostMp(page: number, size: number, keyword?: string, level1TagId?: string, level2TagId?: string, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<PagePost>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.pagePostMp(page, size, keyword, level1TagId, level2TagId, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['PostMpApi.pagePostMp']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
    }
};

/**
 * PostMpApi - factory interface
 * @export
 */
export const PostMpApiFactory = function (configuration?: Configuration, basePath?: string, axios?: AxiosInstance) {
    const localVarFp = PostMpApiFp(configuration)
    return {
        /**
         * 
         * @summary 前台根据id查询帖子
         * @param {PostMpApiGetPostByIdMpRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getPostByIdMp(requestParameters: PostMpApiGetPostByIdMpRequest, options?: RawAxiosRequestConfig): AxiosPromise<Post> {
            return localVarFp.getPostByIdMp(requestParameters.id, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 帖子转发，增加帖子转发量
         * @param {PostMpApiIncrementPostForwardCountMpRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        incrementPostForwardCountMp(requestParameters: PostMpApiIncrementPostForwardCountMpRequest, options?: RawAxiosRequestConfig): AxiosPromise<boolean> {
            return localVarFp.incrementPostForwardCountMp(requestParameters.id, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 增加帖子浏览量
         * @param {PostMpApiIncrementPostViewCountMpRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        incrementPostViewCountMp(requestParameters: PostMpApiIncrementPostViewCountMpRequest, options?: RawAxiosRequestConfig): AxiosPromise<boolean> {
            return localVarFp.incrementPostViewCountMp(requestParameters.id, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 前台分页查询帖子列表
         * @param {PostMpApiPagePostMpRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        pagePostMp(requestParameters: PostMpApiPagePostMpRequest, options?: RawAxiosRequestConfig): AxiosPromise<PagePost> {
            return localVarFp.pagePostMp(requestParameters.page, requestParameters.size, requestParameters.keyword, requestParameters.level1TagId, requestParameters.level2TagId, options).then((request) => request(axios, basePath));
        },
    };
};

/**
 * Request parameters for getPostByIdMp operation in PostMpApi.
 * @export
 * @interface PostMpApiGetPostByIdMpRequest
 */
export interface PostMpApiGetPostByIdMpRequest {
    /**
     * 帖子id
     * @type {string}
     * @memberof PostMpApiGetPostByIdMp
     */
    readonly id: string
}

/**
 * Request parameters for incrementPostForwardCountMp operation in PostMpApi.
 * @export
 * @interface PostMpApiIncrementPostForwardCountMpRequest
 */
export interface PostMpApiIncrementPostForwardCountMpRequest {
    /**
     * 帖子id
     * @type {string}
     * @memberof PostMpApiIncrementPostForwardCountMp
     */
    readonly id: string
}

/**
 * Request parameters for incrementPostViewCountMp operation in PostMpApi.
 * @export
 * @interface PostMpApiIncrementPostViewCountMpRequest
 */
export interface PostMpApiIncrementPostViewCountMpRequest {
    /**
     * 帖子id
     * @type {string}
     * @memberof PostMpApiIncrementPostViewCountMp
     */
    readonly id: string
}

/**
 * Request parameters for pagePostMp operation in PostMpApi.
 * @export
 * @interface PostMpApiPagePostMpRequest
 */
export interface PostMpApiPagePostMpRequest {
    /**
     * 页码，从1开始
     * @type {number}
     * @memberof PostMpApiPagePostMp
     */
    readonly page: number

    /**
     * 每页大小
     * @type {number}
     * @memberof PostMpApiPagePostMp
     */
    readonly size: number

    /**
     * 关键字
     * @type {string}
     * @memberof PostMpApiPagePostMp
     */
    readonly keyword?: string

    /**
     * 一级标签id
     * @type {string}
     * @memberof PostMpApiPagePostMp
     */
    readonly level1TagId?: string

    /**
     * 二级标签id
     * @type {string}
     * @memberof PostMpApiPagePostMp
     */
    readonly level2TagId?: string
}

/**
 * PostMpApi - object-oriented interface
 * @export
 * @class PostMpApi
 * @extends {BaseAPI}
 */
export class PostMpApi extends BaseAPI {
    /**
     * 
     * @summary 前台根据id查询帖子
     * @param {PostMpApiGetPostByIdMpRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof PostMpApi
     */
    public getPostByIdMp(requestParameters: PostMpApiGetPostByIdMpRequest, options?: RawAxiosRequestConfig) {
        return PostMpApiFp(this.configuration).getPostByIdMp(requestParameters.id, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 帖子转发，增加帖子转发量
     * @param {PostMpApiIncrementPostForwardCountMpRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof PostMpApi
     */
    public incrementPostForwardCountMp(requestParameters: PostMpApiIncrementPostForwardCountMpRequest, options?: RawAxiosRequestConfig) {
        return PostMpApiFp(this.configuration).incrementPostForwardCountMp(requestParameters.id, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 增加帖子浏览量
     * @param {PostMpApiIncrementPostViewCountMpRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof PostMpApi
     */
    public incrementPostViewCountMp(requestParameters: PostMpApiIncrementPostViewCountMpRequest, options?: RawAxiosRequestConfig) {
        return PostMpApiFp(this.configuration).incrementPostViewCountMp(requestParameters.id, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 前台分页查询帖子列表
     * @param {PostMpApiPagePostMpRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof PostMpApi
     */
    public pagePostMp(requestParameters: PostMpApiPagePostMpRequest, options?: RawAxiosRequestConfig) {
        return PostMpApiFp(this.configuration).pagePostMp(requestParameters.page, requestParameters.size, requestParameters.keyword, requestParameters.level1TagId, requestParameters.level2TagId, options).then((request) => request(this.axios, this.basePath));
    }
}



/**
 * PostTagAdminApi - axios parameter creator
 * @export
 */
export const PostTagAdminApiAxiosParamCreator = function (configuration?: Configuration) {
    return {
        /**
         * 
         * @summary 新增帖子标签
         * @param {PostTagCreateRequest} postTagCreateRequest 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        createPostTagAdmin: async (postTagCreateRequest: PostTagCreateRequest, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'postTagCreateRequest' is not null or undefined
            assertParamExists('createPostTagAdmin', 'postTagCreateRequest', postTagCreateRequest)
            const localVarPath = `/api/v1/admin/post-tag`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'POST', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            localVarHeaderParameter['Content-Type'] = 'application/json';

            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };
            localVarRequestOptions.data = serializeDataIfNeeded(postTagCreateRequest, localVarRequestOptions, configuration)

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 根据id删除帖子标签
         * @param {string} id 标签id
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        deletePostTagByIdAdmin: async (id: string, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'id' is not null or undefined
            assertParamExists('deletePostTagByIdAdmin', 'id', id)
            const localVarPath = `/api/v1/admin/post-tag/{id}`
                .replace(`{${"id"}}`, encodeURIComponent(String(id)));
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'DELETE', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 根据id查询帖子标签
         * @param {string} id 标签id
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getPostTagByIdAdmin: async (id: string, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'id' is not null or undefined
            assertParamExists('getPostTagByIdAdmin', 'id', id)
            const localVarPath = `/api/v1/admin/post-tag/{id}`
                .replace(`{${"id"}}`, encodeURIComponent(String(id)));
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 查询帖子标签列表，构建层级关系
         * @param {boolean} [needCountPost] 是否需要计算帖子数量
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        listPostTagAdmin: async (needCountPost?: boolean, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            const localVarPath = `/api/v1/admin/post-tag`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)

            if (needCountPost !== undefined) {
                localVarQueryParameter['needCountPost'] = needCountPost;
            }



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 修改帖子标签
         * @param {string} id 标签id
         * @param {PostTagUpdateRequest} postTagUpdateRequest 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        updatePostTagAdmin: async (id: string, postTagUpdateRequest: PostTagUpdateRequest, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'id' is not null or undefined
            assertParamExists('updatePostTagAdmin', 'id', id)
            // verify required parameter 'postTagUpdateRequest' is not null or undefined
            assertParamExists('updatePostTagAdmin', 'postTagUpdateRequest', postTagUpdateRequest)
            const localVarPath = `/api/v1/admin/post-tag/{id}`
                .replace(`{${"id"}}`, encodeURIComponent(String(id)));
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'PUT', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            localVarHeaderParameter['Content-Type'] = 'application/json';

            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };
            localVarRequestOptions.data = serializeDataIfNeeded(postTagUpdateRequest, localVarRequestOptions, configuration)

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
    }
};

/**
 * PostTagAdminApi - functional programming interface
 * @export
 */
export const PostTagAdminApiFp = function (configuration?: Configuration) {
    const localVarAxiosParamCreator = PostTagAdminApiAxiosParamCreator(configuration)
    return {
        /**
         * 
         * @summary 新增帖子标签
         * @param {PostTagCreateRequest} postTagCreateRequest 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async createPostTagAdmin(postTagCreateRequest: PostTagCreateRequest, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<PostTag>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.createPostTagAdmin(postTagCreateRequest, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['PostTagAdminApi.createPostTagAdmin']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 根据id删除帖子标签
         * @param {string} id 标签id
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async deletePostTagByIdAdmin(id: string, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<boolean>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.deletePostTagByIdAdmin(id, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['PostTagAdminApi.deletePostTagByIdAdmin']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 根据id查询帖子标签
         * @param {string} id 标签id
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async getPostTagByIdAdmin(id: string, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<PostTag>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.getPostTagByIdAdmin(id, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['PostTagAdminApi.getPostTagByIdAdmin']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 查询帖子标签列表，构建层级关系
         * @param {boolean} [needCountPost] 是否需要计算帖子数量
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async listPostTagAdmin(needCountPost?: boolean, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<Array<PostTag>>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.listPostTagAdmin(needCountPost, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['PostTagAdminApi.listPostTagAdmin']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 修改帖子标签
         * @param {string} id 标签id
         * @param {PostTagUpdateRequest} postTagUpdateRequest 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async updatePostTagAdmin(id: string, postTagUpdateRequest: PostTagUpdateRequest, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<boolean>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.updatePostTagAdmin(id, postTagUpdateRequest, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['PostTagAdminApi.updatePostTagAdmin']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
    }
};

/**
 * PostTagAdminApi - factory interface
 * @export
 */
export const PostTagAdminApiFactory = function (configuration?: Configuration, basePath?: string, axios?: AxiosInstance) {
    const localVarFp = PostTagAdminApiFp(configuration)
    return {
        /**
         * 
         * @summary 新增帖子标签
         * @param {PostTagAdminApiCreatePostTagAdminRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        createPostTagAdmin(requestParameters: PostTagAdminApiCreatePostTagAdminRequest, options?: RawAxiosRequestConfig): AxiosPromise<PostTag> {
            return localVarFp.createPostTagAdmin(requestParameters.postTagCreateRequest, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 根据id删除帖子标签
         * @param {PostTagAdminApiDeletePostTagByIdAdminRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        deletePostTagByIdAdmin(requestParameters: PostTagAdminApiDeletePostTagByIdAdminRequest, options?: RawAxiosRequestConfig): AxiosPromise<boolean> {
            return localVarFp.deletePostTagByIdAdmin(requestParameters.id, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 根据id查询帖子标签
         * @param {PostTagAdminApiGetPostTagByIdAdminRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getPostTagByIdAdmin(requestParameters: PostTagAdminApiGetPostTagByIdAdminRequest, options?: RawAxiosRequestConfig): AxiosPromise<PostTag> {
            return localVarFp.getPostTagByIdAdmin(requestParameters.id, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 查询帖子标签列表，构建层级关系
         * @param {PostTagAdminApiListPostTagAdminRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        listPostTagAdmin(requestParameters: PostTagAdminApiListPostTagAdminRequest = {}, options?: RawAxiosRequestConfig): AxiosPromise<Array<PostTag>> {
            return localVarFp.listPostTagAdmin(requestParameters.needCountPost, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 修改帖子标签
         * @param {PostTagAdminApiUpdatePostTagAdminRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        updatePostTagAdmin(requestParameters: PostTagAdminApiUpdatePostTagAdminRequest, options?: RawAxiosRequestConfig): AxiosPromise<boolean> {
            return localVarFp.updatePostTagAdmin(requestParameters.id, requestParameters.postTagUpdateRequest, options).then((request) => request(axios, basePath));
        },
    };
};

/**
 * Request parameters for createPostTagAdmin operation in PostTagAdminApi.
 * @export
 * @interface PostTagAdminApiCreatePostTagAdminRequest
 */
export interface PostTagAdminApiCreatePostTagAdminRequest {
    /**
     * 
     * @type {PostTagCreateRequest}
     * @memberof PostTagAdminApiCreatePostTagAdmin
     */
    readonly postTagCreateRequest: PostTagCreateRequest
}

/**
 * Request parameters for deletePostTagByIdAdmin operation in PostTagAdminApi.
 * @export
 * @interface PostTagAdminApiDeletePostTagByIdAdminRequest
 */
export interface PostTagAdminApiDeletePostTagByIdAdminRequest {
    /**
     * 标签id
     * @type {string}
     * @memberof PostTagAdminApiDeletePostTagByIdAdmin
     */
    readonly id: string
}

/**
 * Request parameters for getPostTagByIdAdmin operation in PostTagAdminApi.
 * @export
 * @interface PostTagAdminApiGetPostTagByIdAdminRequest
 */
export interface PostTagAdminApiGetPostTagByIdAdminRequest {
    /**
     * 标签id
     * @type {string}
     * @memberof PostTagAdminApiGetPostTagByIdAdmin
     */
    readonly id: string
}

/**
 * Request parameters for listPostTagAdmin operation in PostTagAdminApi.
 * @export
 * @interface PostTagAdminApiListPostTagAdminRequest
 */
export interface PostTagAdminApiListPostTagAdminRequest {
    /**
     * 是否需要计算帖子数量
     * @type {boolean}
     * @memberof PostTagAdminApiListPostTagAdmin
     */
    readonly needCountPost?: boolean
}

/**
 * Request parameters for updatePostTagAdmin operation in PostTagAdminApi.
 * @export
 * @interface PostTagAdminApiUpdatePostTagAdminRequest
 */
export interface PostTagAdminApiUpdatePostTagAdminRequest {
    /**
     * 标签id
     * @type {string}
     * @memberof PostTagAdminApiUpdatePostTagAdmin
     */
    readonly id: string

    /**
     * 
     * @type {PostTagUpdateRequest}
     * @memberof PostTagAdminApiUpdatePostTagAdmin
     */
    readonly postTagUpdateRequest: PostTagUpdateRequest
}

/**
 * PostTagAdminApi - object-oriented interface
 * @export
 * @class PostTagAdminApi
 * @extends {BaseAPI}
 */
export class PostTagAdminApi extends BaseAPI {
    /**
     * 
     * @summary 新增帖子标签
     * @param {PostTagAdminApiCreatePostTagAdminRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof PostTagAdminApi
     */
    public createPostTagAdmin(requestParameters: PostTagAdminApiCreatePostTagAdminRequest, options?: RawAxiosRequestConfig) {
        return PostTagAdminApiFp(this.configuration).createPostTagAdmin(requestParameters.postTagCreateRequest, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 根据id删除帖子标签
     * @param {PostTagAdminApiDeletePostTagByIdAdminRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof PostTagAdminApi
     */
    public deletePostTagByIdAdmin(requestParameters: PostTagAdminApiDeletePostTagByIdAdminRequest, options?: RawAxiosRequestConfig) {
        return PostTagAdminApiFp(this.configuration).deletePostTagByIdAdmin(requestParameters.id, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 根据id查询帖子标签
     * @param {PostTagAdminApiGetPostTagByIdAdminRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof PostTagAdminApi
     */
    public getPostTagByIdAdmin(requestParameters: PostTagAdminApiGetPostTagByIdAdminRequest, options?: RawAxiosRequestConfig) {
        return PostTagAdminApiFp(this.configuration).getPostTagByIdAdmin(requestParameters.id, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 查询帖子标签列表，构建层级关系
     * @param {PostTagAdminApiListPostTagAdminRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof PostTagAdminApi
     */
    public listPostTagAdmin(requestParameters: PostTagAdminApiListPostTagAdminRequest = {}, options?: RawAxiosRequestConfig) {
        return PostTagAdminApiFp(this.configuration).listPostTagAdmin(requestParameters.needCountPost, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 修改帖子标签
     * @param {PostTagAdminApiUpdatePostTagAdminRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof PostTagAdminApi
     */
    public updatePostTagAdmin(requestParameters: PostTagAdminApiUpdatePostTagAdminRequest, options?: RawAxiosRequestConfig) {
        return PostTagAdminApiFp(this.configuration).updatePostTagAdmin(requestParameters.id, requestParameters.postTagUpdateRequest, options).then((request) => request(this.axios, this.basePath));
    }
}



/**
 * PostTagMpApi - axios parameter creator
 * @export
 */
export const PostTagMpApiAxiosParamCreator = function (configuration?: Configuration) {
    return {
        /**
         * 
         * @summary 根据id查询帖子标签
         * @param {string} id 标签id
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getPostTagByIdMp: async (id: string, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'id' is not null or undefined
            assertParamExists('getPostTagByIdMp', 'id', id)
            const localVarPath = `/api/v1/mp/post-tag/{id}`
                .replace(`{${"id"}}`, encodeURIComponent(String(id)));
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 查询帖子标签列表，构建层级关系
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        listPostTagMp: async (options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            const localVarPath = `/api/v1/mp/post-tag`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
    }
};

/**
 * PostTagMpApi - functional programming interface
 * @export
 */
export const PostTagMpApiFp = function (configuration?: Configuration) {
    const localVarAxiosParamCreator = PostTagMpApiAxiosParamCreator(configuration)
    return {
        /**
         * 
         * @summary 根据id查询帖子标签
         * @param {string} id 标签id
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async getPostTagByIdMp(id: string, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<PostTag>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.getPostTagByIdMp(id, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['PostTagMpApi.getPostTagByIdMp']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 查询帖子标签列表，构建层级关系
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async listPostTagMp(options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<Array<PostTag>>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.listPostTagMp(options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['PostTagMpApi.listPostTagMp']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
    }
};

/**
 * PostTagMpApi - factory interface
 * @export
 */
export const PostTagMpApiFactory = function (configuration?: Configuration, basePath?: string, axios?: AxiosInstance) {
    const localVarFp = PostTagMpApiFp(configuration)
    return {
        /**
         * 
         * @summary 根据id查询帖子标签
         * @param {PostTagMpApiGetPostTagByIdMpRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getPostTagByIdMp(requestParameters: PostTagMpApiGetPostTagByIdMpRequest, options?: RawAxiosRequestConfig): AxiosPromise<PostTag> {
            return localVarFp.getPostTagByIdMp(requestParameters.id, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 查询帖子标签列表，构建层级关系
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        listPostTagMp(options?: RawAxiosRequestConfig): AxiosPromise<Array<PostTag>> {
            return localVarFp.listPostTagMp(options).then((request) => request(axios, basePath));
        },
    };
};

/**
 * Request parameters for getPostTagByIdMp operation in PostTagMpApi.
 * @export
 * @interface PostTagMpApiGetPostTagByIdMpRequest
 */
export interface PostTagMpApiGetPostTagByIdMpRequest {
    /**
     * 标签id
     * @type {string}
     * @memberof PostTagMpApiGetPostTagByIdMp
     */
    readonly id: string
}

/**
 * PostTagMpApi - object-oriented interface
 * @export
 * @class PostTagMpApi
 * @extends {BaseAPI}
 */
export class PostTagMpApi extends BaseAPI {
    /**
     * 
     * @summary 根据id查询帖子标签
     * @param {PostTagMpApiGetPostTagByIdMpRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof PostTagMpApi
     */
    public getPostTagByIdMp(requestParameters: PostTagMpApiGetPostTagByIdMpRequest, options?: RawAxiosRequestConfig) {
        return PostTagMpApiFp(this.configuration).getPostTagByIdMp(requestParameters.id, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 查询帖子标签列表，构建层级关系
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof PostTagMpApi
     */
    public listPostTagMp(options?: RawAxiosRequestConfig) {
        return PostTagMpApiFp(this.configuration).listPostTagMp(options).then((request) => request(this.axios, this.basePath));
    }
}



/**
 * PostUserRelationMpApi - axios parameter creator
 * @export
 */
export const PostUserRelationMpApiAxiosParamCreator = function (configuration?: Configuration) {
    return {
        /**
         * 
         * @summary 创建用户与帖子的关联
         * @param {PostUserRelationChangeRequest} postUserRelationChangeRequest 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        createPostUserRelationMp: async (postUserRelationChangeRequest: PostUserRelationChangeRequest, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'postUserRelationChangeRequest' is not null or undefined
            assertParamExists('createPostUserRelationMp', 'postUserRelationChangeRequest', postUserRelationChangeRequest)
            const localVarPath = `/api/v1/mp/post-user-relation`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'POST', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            localVarHeaderParameter['Content-Type'] = 'application/json';

            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };
            localVarRequestOptions.data = serializeDataIfNeeded(postUserRelationChangeRequest, localVarRequestOptions, configuration)

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 删除用户与帖子的关联
         * @param {PostUserRelationChangeRequest} postUserRelationChangeRequest 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        deletePostUserRelationMp: async (postUserRelationChangeRequest: PostUserRelationChangeRequest, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'postUserRelationChangeRequest' is not null or undefined
            assertParamExists('deletePostUserRelationMp', 'postUserRelationChangeRequest', postUserRelationChangeRequest)
            const localVarPath = `/api/v1/mp/post-user-relation`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'DELETE', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            localVarHeaderParameter['Content-Type'] = 'application/json';

            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };
            localVarRequestOptions.data = serializeDataIfNeeded(postUserRelationChangeRequest, localVarRequestOptions, configuration)

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 分页查询用户收藏的帖子列表
         * @param {number} page 页码，从1开始
         * @param {number} size 每页大小
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        pageCollectPostUserRelationMp: async (page: number, size: number, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'page' is not null or undefined
            assertParamExists('pageCollectPostUserRelationMp', 'page', page)
            // verify required parameter 'size' is not null or undefined
            assertParamExists('pageCollectPostUserRelationMp', 'size', size)
            const localVarPath = `/api/v1/mp/post-user-relation/collect-page`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)

            if (page !== undefined) {
                localVarQueryParameter['page'] = page;
            }

            if (size !== undefined) {
                localVarQueryParameter['size'] = size;
            }



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
    }
};

/**
 * PostUserRelationMpApi - functional programming interface
 * @export
 */
export const PostUserRelationMpApiFp = function (configuration?: Configuration) {
    const localVarAxiosParamCreator = PostUserRelationMpApiAxiosParamCreator(configuration)
    return {
        /**
         * 
         * @summary 创建用户与帖子的关联
         * @param {PostUserRelationChangeRequest} postUserRelationChangeRequest 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async createPostUserRelationMp(postUserRelationChangeRequest: PostUserRelationChangeRequest, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<PostUserRelation>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.createPostUserRelationMp(postUserRelationChangeRequest, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['PostUserRelationMpApi.createPostUserRelationMp']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 删除用户与帖子的关联
         * @param {PostUserRelationChangeRequest} postUserRelationChangeRequest 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async deletePostUserRelationMp(postUserRelationChangeRequest: PostUserRelationChangeRequest, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<boolean>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.deletePostUserRelationMp(postUserRelationChangeRequest, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['PostUserRelationMpApi.deletePostUserRelationMp']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 分页查询用户收藏的帖子列表
         * @param {number} page 页码，从1开始
         * @param {number} size 每页大小
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async pageCollectPostUserRelationMp(page: number, size: number, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<PagePostUserRelation>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.pageCollectPostUserRelationMp(page, size, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['PostUserRelationMpApi.pageCollectPostUserRelationMp']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
    }
};

/**
 * PostUserRelationMpApi - factory interface
 * @export
 */
export const PostUserRelationMpApiFactory = function (configuration?: Configuration, basePath?: string, axios?: AxiosInstance) {
    const localVarFp = PostUserRelationMpApiFp(configuration)
    return {
        /**
         * 
         * @summary 创建用户与帖子的关联
         * @param {PostUserRelationMpApiCreatePostUserRelationMpRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        createPostUserRelationMp(requestParameters: PostUserRelationMpApiCreatePostUserRelationMpRequest, options?: RawAxiosRequestConfig): AxiosPromise<PostUserRelation> {
            return localVarFp.createPostUserRelationMp(requestParameters.postUserRelationChangeRequest, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 删除用户与帖子的关联
         * @param {PostUserRelationMpApiDeletePostUserRelationMpRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        deletePostUserRelationMp(requestParameters: PostUserRelationMpApiDeletePostUserRelationMpRequest, options?: RawAxiosRequestConfig): AxiosPromise<boolean> {
            return localVarFp.deletePostUserRelationMp(requestParameters.postUserRelationChangeRequest, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 分页查询用户收藏的帖子列表
         * @param {PostUserRelationMpApiPageCollectPostUserRelationMpRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        pageCollectPostUserRelationMp(requestParameters: PostUserRelationMpApiPageCollectPostUserRelationMpRequest, options?: RawAxiosRequestConfig): AxiosPromise<PagePostUserRelation> {
            return localVarFp.pageCollectPostUserRelationMp(requestParameters.page, requestParameters.size, options).then((request) => request(axios, basePath));
        },
    };
};

/**
 * Request parameters for createPostUserRelationMp operation in PostUserRelationMpApi.
 * @export
 * @interface PostUserRelationMpApiCreatePostUserRelationMpRequest
 */
export interface PostUserRelationMpApiCreatePostUserRelationMpRequest {
    /**
     * 
     * @type {PostUserRelationChangeRequest}
     * @memberof PostUserRelationMpApiCreatePostUserRelationMp
     */
    readonly postUserRelationChangeRequest: PostUserRelationChangeRequest
}

/**
 * Request parameters for deletePostUserRelationMp operation in PostUserRelationMpApi.
 * @export
 * @interface PostUserRelationMpApiDeletePostUserRelationMpRequest
 */
export interface PostUserRelationMpApiDeletePostUserRelationMpRequest {
    /**
     * 
     * @type {PostUserRelationChangeRequest}
     * @memberof PostUserRelationMpApiDeletePostUserRelationMp
     */
    readonly postUserRelationChangeRequest: PostUserRelationChangeRequest
}

/**
 * Request parameters for pageCollectPostUserRelationMp operation in PostUserRelationMpApi.
 * @export
 * @interface PostUserRelationMpApiPageCollectPostUserRelationMpRequest
 */
export interface PostUserRelationMpApiPageCollectPostUserRelationMpRequest {
    /**
     * 页码，从1开始
     * @type {number}
     * @memberof PostUserRelationMpApiPageCollectPostUserRelationMp
     */
    readonly page: number

    /**
     * 每页大小
     * @type {number}
     * @memberof PostUserRelationMpApiPageCollectPostUserRelationMp
     */
    readonly size: number
}

/**
 * PostUserRelationMpApi - object-oriented interface
 * @export
 * @class PostUserRelationMpApi
 * @extends {BaseAPI}
 */
export class PostUserRelationMpApi extends BaseAPI {
    /**
     * 
     * @summary 创建用户与帖子的关联
     * @param {PostUserRelationMpApiCreatePostUserRelationMpRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof PostUserRelationMpApi
     */
    public createPostUserRelationMp(requestParameters: PostUserRelationMpApiCreatePostUserRelationMpRequest, options?: RawAxiosRequestConfig) {
        return PostUserRelationMpApiFp(this.configuration).createPostUserRelationMp(requestParameters.postUserRelationChangeRequest, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 删除用户与帖子的关联
     * @param {PostUserRelationMpApiDeletePostUserRelationMpRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof PostUserRelationMpApi
     */
    public deletePostUserRelationMp(requestParameters: PostUserRelationMpApiDeletePostUserRelationMpRequest, options?: RawAxiosRequestConfig) {
        return PostUserRelationMpApiFp(this.configuration).deletePostUserRelationMp(requestParameters.postUserRelationChangeRequest, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 分页查询用户收藏的帖子列表
     * @param {PostUserRelationMpApiPageCollectPostUserRelationMpRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof PostUserRelationMpApi
     */
    public pageCollectPostUserRelationMp(requestParameters: PostUserRelationMpApiPageCollectPostUserRelationMpRequest, options?: RawAxiosRequestConfig) {
        return PostUserRelationMpApiFp(this.configuration).pageCollectPostUserRelationMp(requestParameters.page, requestParameters.size, options).then((request) => request(this.axios, this.basePath));
    }
}



/**
 * QALottoApi - axios parameter creator
 * @export
 */
export const QALottoApiAxiosParamCreator = function (configuration?: Configuration) {
    return {
        /**
         * 
         * @summary 清除抽奖记录
         * @param {string} activityId 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        clearLotteryRecord: async (activityId: string, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'activityId' is not null or undefined
            assertParamExists('clearLotteryRecord', 'activityId', activityId)
            const localVarPath = `/api/v1/qa/lotto/lottery-records`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'DELETE', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)

            if (activityId !== undefined) {
                localVarQueryParameter['activityId'] = activityId;
            }



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 清除用户抽奖记录
         * @param {string} user 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        clearUserLotteryRecord: async (user: string, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'user' is not null or undefined
            assertParamExists('clearUserLotteryRecord', 'user', user)
            const localVarPath = `/api/v1/qa/lotto/lottery-user-records`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'DELETE', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)

            if (user !== undefined) {
                localVarQueryParameter['user'] = user;
            }



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
    }
};

/**
 * QALottoApi - functional programming interface
 * @export
 */
export const QALottoApiFp = function (configuration?: Configuration) {
    const localVarAxiosParamCreator = QALottoApiAxiosParamCreator(configuration)
    return {
        /**
         * 
         * @summary 清除抽奖记录
         * @param {string} activityId 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async clearLotteryRecord(activityId: string, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<void>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.clearLotteryRecord(activityId, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['QALottoApi.clearLotteryRecord']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 清除用户抽奖记录
         * @param {string} user 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async clearUserLotteryRecord(user: string, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<void>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.clearUserLotteryRecord(user, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['QALottoApi.clearUserLotteryRecord']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
    }
};

/**
 * QALottoApi - factory interface
 * @export
 */
export const QALottoApiFactory = function (configuration?: Configuration, basePath?: string, axios?: AxiosInstance) {
    const localVarFp = QALottoApiFp(configuration)
    return {
        /**
         * 
         * @summary 清除抽奖记录
         * @param {QALottoApiClearLotteryRecordRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        clearLotteryRecord(requestParameters: QALottoApiClearLotteryRecordRequest, options?: RawAxiosRequestConfig): AxiosPromise<void> {
            return localVarFp.clearLotteryRecord(requestParameters.activityId, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 清除用户抽奖记录
         * @param {QALottoApiClearUserLotteryRecordRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        clearUserLotteryRecord(requestParameters: QALottoApiClearUserLotteryRecordRequest, options?: RawAxiosRequestConfig): AxiosPromise<void> {
            return localVarFp.clearUserLotteryRecord(requestParameters.user, options).then((request) => request(axios, basePath));
        },
    };
};

/**
 * Request parameters for clearLotteryRecord operation in QALottoApi.
 * @export
 * @interface QALottoApiClearLotteryRecordRequest
 */
export interface QALottoApiClearLotteryRecordRequest {
    /**
     * 
     * @type {string}
     * @memberof QALottoApiClearLotteryRecord
     */
    readonly activityId: string
}

/**
 * Request parameters for clearUserLotteryRecord operation in QALottoApi.
 * @export
 * @interface QALottoApiClearUserLotteryRecordRequest
 */
export interface QALottoApiClearUserLotteryRecordRequest {
    /**
     * 
     * @type {string}
     * @memberof QALottoApiClearUserLotteryRecord
     */
    readonly user: string
}

/**
 * QALottoApi - object-oriented interface
 * @export
 * @class QALottoApi
 * @extends {BaseAPI}
 */
export class QALottoApi extends BaseAPI {
    /**
     * 
     * @summary 清除抽奖记录
     * @param {QALottoApiClearLotteryRecordRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof QALottoApi
     */
    public clearLotteryRecord(requestParameters: QALottoApiClearLotteryRecordRequest, options?: RawAxiosRequestConfig) {
        return QALottoApiFp(this.configuration).clearLotteryRecord(requestParameters.activityId, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 清除用户抽奖记录
     * @param {QALottoApiClearUserLotteryRecordRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof QALottoApi
     */
    public clearUserLotteryRecord(requestParameters: QALottoApiClearUserLotteryRecordRequest, options?: RawAxiosRequestConfig) {
        return QALottoApiFp(this.configuration).clearUserLotteryRecord(requestParameters.user, options).then((request) => request(this.axios, this.basePath));
    }
}



/**
 * QaFakeTimeApi - axios parameter creator
 * @export
 */
export const QaFakeTimeApiAxiosParamCreator = function (configuration?: Configuration) {
    return {
        /**
         * 
         * @summary 获取当前虚拟时间。
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getFaketime: async (options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            const localVarPath = `/api/v1/qa/faketime`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 重置当前虚拟时间。
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        resetFaketime: async (options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            const localVarPath = `/api/v1/qa/faketime`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'DELETE', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 设置虚拟时间。完整 ISO 时间字符串，如：2023-07-04T11:56:06.244+08:00，或者当前时间偏移量，如：+3600、-3600 单位为秒。或者带上单位，如 +3600s[m/h/d/w/M/y]，分别表示 秒[分钟/小时/天/周/月/年]。
         * @param {string} faketime 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        setFaketime: async (faketime: string, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'faketime' is not null or undefined
            assertParamExists('setFaketime', 'faketime', faketime)
            const localVarPath = `/api/v1/qa/faketime`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'PUT', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)

            if (faketime !== undefined) {
                localVarQueryParameter['faketime'] = faketime;
            }



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
    }
};

/**
 * QaFakeTimeApi - functional programming interface
 * @export
 */
export const QaFakeTimeApiFp = function (configuration?: Configuration) {
    const localVarAxiosParamCreator = QaFakeTimeApiAxiosParamCreator(configuration)
    return {
        /**
         * 
         * @summary 获取当前虚拟时间。
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async getFaketime(options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<string>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.getFaketime(options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['QaFakeTimeApi.getFaketime']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 重置当前虚拟时间。
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async resetFaketime(options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<string>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.resetFaketime(options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['QaFakeTimeApi.resetFaketime']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 设置虚拟时间。完整 ISO 时间字符串，如：2023-07-04T11:56:06.244+08:00，或者当前时间偏移量，如：+3600、-3600 单位为秒。或者带上单位，如 +3600s[m/h/d/w/M/y]，分别表示 秒[分钟/小时/天/周/月/年]。
         * @param {string} faketime 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async setFaketime(faketime: string, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<string>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.setFaketime(faketime, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['QaFakeTimeApi.setFaketime']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
    }
};

/**
 * QaFakeTimeApi - factory interface
 * @export
 */
export const QaFakeTimeApiFactory = function (configuration?: Configuration, basePath?: string, axios?: AxiosInstance) {
    const localVarFp = QaFakeTimeApiFp(configuration)
    return {
        /**
         * 
         * @summary 获取当前虚拟时间。
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getFaketime(options?: RawAxiosRequestConfig): AxiosPromise<string> {
            return localVarFp.getFaketime(options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 重置当前虚拟时间。
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        resetFaketime(options?: RawAxiosRequestConfig): AxiosPromise<string> {
            return localVarFp.resetFaketime(options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 设置虚拟时间。完整 ISO 时间字符串，如：2023-07-04T11:56:06.244+08:00，或者当前时间偏移量，如：+3600、-3600 单位为秒。或者带上单位，如 +3600s[m/h/d/w/M/y]，分别表示 秒[分钟/小时/天/周/月/年]。
         * @param {QaFakeTimeApiSetFaketimeRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        setFaketime(requestParameters: QaFakeTimeApiSetFaketimeRequest, options?: RawAxiosRequestConfig): AxiosPromise<string> {
            return localVarFp.setFaketime(requestParameters.faketime, options).then((request) => request(axios, basePath));
        },
    };
};

/**
 * Request parameters for setFaketime operation in QaFakeTimeApi.
 * @export
 * @interface QaFakeTimeApiSetFaketimeRequest
 */
export interface QaFakeTimeApiSetFaketimeRequest {
    /**
     * 
     * @type {string}
     * @memberof QaFakeTimeApiSetFaketime
     */
    readonly faketime: string
}

/**
 * QaFakeTimeApi - object-oriented interface
 * @export
 * @class QaFakeTimeApi
 * @extends {BaseAPI}
 */
export class QaFakeTimeApi extends BaseAPI {
    /**
     * 
     * @summary 获取当前虚拟时间。
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof QaFakeTimeApi
     */
    public getFaketime(options?: RawAxiosRequestConfig) {
        return QaFakeTimeApiFp(this.configuration).getFaketime(options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 重置当前虚拟时间。
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof QaFakeTimeApi
     */
    public resetFaketime(options?: RawAxiosRequestConfig) {
        return QaFakeTimeApiFp(this.configuration).resetFaketime(options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 设置虚拟时间。完整 ISO 时间字符串，如：2023-07-04T11:56:06.244+08:00，或者当前时间偏移量，如：+3600、-3600 单位为秒。或者带上单位，如 +3600s[m/h/d/w/M/y]，分别表示 秒[分钟/小时/天/周/月/年]。
     * @param {QaFakeTimeApiSetFaketimeRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof QaFakeTimeApi
     */
    public setFaketime(requestParameters: QaFakeTimeApiSetFaketimeRequest, options?: RawAxiosRequestConfig) {
        return QaFakeTimeApiFp(this.configuration).setFaketime(requestParameters.faketime, options).then((request) => request(this.axios, this.basePath));
    }
}



/**
 * QaUserPointApi - axios parameter creator
 * @export
 */
export const QaUserPointApiAxiosParamCreator = function (configuration?: Configuration) {
    return {
        /**
         * 
         * @summary 获取用户数值。
         * @param {string} key 
         * @param {string} user 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getUserPoint: async (key: string, user: string, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'key' is not null or undefined
            assertParamExists('getUserPoint', 'key', key)
            // verify required parameter 'user' is not null or undefined
            assertParamExists('getUserPoint', 'user', user)
            const localVarPath = `/api/v1/qa/user-points/keys/{key}`
                .replace(`{${"key"}}`, encodeURIComponent(String(key)));
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)

            if (user !== undefined) {
                localVarQueryParameter['user'] = user;
            }



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 为用户增加数值。
         * @param {string} key 
         * @param {string} user 
         * @param {number} value 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getUserPointKeys: async (key: string, user: string, value: number, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'key' is not null or undefined
            assertParamExists('getUserPointKeys', 'key', key)
            // verify required parameter 'user' is not null or undefined
            assertParamExists('getUserPointKeys', 'user', user)
            // verify required parameter 'value' is not null or undefined
            assertParamExists('getUserPointKeys', 'value', value)
            const localVarPath = `/api/v1/qa/user-points/keys/{key}/increase`
                .replace(`{${"key"}}`, encodeURIComponent(String(key)));
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'POST', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)

            if (user !== undefined) {
                localVarQueryParameter['user'] = user;
            }

            if (value !== undefined) {
                localVarQueryParameter['value'] = value;
            }



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
    }
};

/**
 * QaUserPointApi - functional programming interface
 * @export
 */
export const QaUserPointApiFp = function (configuration?: Configuration) {
    const localVarAxiosParamCreator = QaUserPointApiAxiosParamCreator(configuration)
    return {
        /**
         * 
         * @summary 获取用户数值。
         * @param {string} key 
         * @param {string} user 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async getUserPoint(key: string, user: string, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<UserPoint>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.getUserPoint(key, user, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['QaUserPointApi.getUserPoint']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 为用户增加数值。
         * @param {string} key 
         * @param {string} user 
         * @param {number} value 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async getUserPointKeys(key: string, user: string, value: number, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<UserPoint>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.getUserPointKeys(key, user, value, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['QaUserPointApi.getUserPointKeys']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
    }
};

/**
 * QaUserPointApi - factory interface
 * @export
 */
export const QaUserPointApiFactory = function (configuration?: Configuration, basePath?: string, axios?: AxiosInstance) {
    const localVarFp = QaUserPointApiFp(configuration)
    return {
        /**
         * 
         * @summary 获取用户数值。
         * @param {QaUserPointApiGetUserPointRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getUserPoint(requestParameters: QaUserPointApiGetUserPointRequest, options?: RawAxiosRequestConfig): AxiosPromise<UserPoint> {
            return localVarFp.getUserPoint(requestParameters.key, requestParameters.user, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 为用户增加数值。
         * @param {QaUserPointApiGetUserPointKeysRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getUserPointKeys(requestParameters: QaUserPointApiGetUserPointKeysRequest, options?: RawAxiosRequestConfig): AxiosPromise<UserPoint> {
            return localVarFp.getUserPointKeys(requestParameters.key, requestParameters.user, requestParameters.value, options).then((request) => request(axios, basePath));
        },
    };
};

/**
 * Request parameters for getUserPoint operation in QaUserPointApi.
 * @export
 * @interface QaUserPointApiGetUserPointRequest
 */
export interface QaUserPointApiGetUserPointRequest {
    /**
     * 
     * @type {string}
     * @memberof QaUserPointApiGetUserPoint
     */
    readonly key: string

    /**
     * 
     * @type {string}
     * @memberof QaUserPointApiGetUserPoint
     */
    readonly user: string
}

/**
 * Request parameters for getUserPointKeys operation in QaUserPointApi.
 * @export
 * @interface QaUserPointApiGetUserPointKeysRequest
 */
export interface QaUserPointApiGetUserPointKeysRequest {
    /**
     * 
     * @type {string}
     * @memberof QaUserPointApiGetUserPointKeys
     */
    readonly key: string

    /**
     * 
     * @type {string}
     * @memberof QaUserPointApiGetUserPointKeys
     */
    readonly user: string

    /**
     * 
     * @type {number}
     * @memberof QaUserPointApiGetUserPointKeys
     */
    readonly value: number
}

/**
 * QaUserPointApi - object-oriented interface
 * @export
 * @class QaUserPointApi
 * @extends {BaseAPI}
 */
export class QaUserPointApi extends BaseAPI {
    /**
     * 
     * @summary 获取用户数值。
     * @param {QaUserPointApiGetUserPointRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof QaUserPointApi
     */
    public getUserPoint(requestParameters: QaUserPointApiGetUserPointRequest, options?: RawAxiosRequestConfig) {
        return QaUserPointApiFp(this.configuration).getUserPoint(requestParameters.key, requestParameters.user, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 为用户增加数值。
     * @param {QaUserPointApiGetUserPointKeysRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof QaUserPointApi
     */
    public getUserPointKeys(requestParameters: QaUserPointApiGetUserPointKeysRequest, options?: RawAxiosRequestConfig) {
        return QaUserPointApiFp(this.configuration).getUserPointKeys(requestParameters.key, requestParameters.user, requestParameters.value, options).then((request) => request(this.axios, this.basePath));
    }
}



/**
 * RoleActivenessGameApi - axios parameter creator
 * @export
 */
export const RoleActivenessGameApiAxiosParamCreator = function (configuration?: Configuration) {
    return {
        /**
         * 
         * @summary 更新角色每日活跃度
         * @param {string} xAppId 应用ID
         * @param {string} xAppSignature 应用签名
         * @param {string} xAppDate 应用时间戳
         * @param {RoleActivenessSaveRequest} roleActivenessSaveRequest 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        updateRoleActiveness: async (xAppId: string, xAppSignature: string, xAppDate: string, roleActivenessSaveRequest: RoleActivenessSaveRequest, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'xAppId' is not null or undefined
            assertParamExists('updateRoleActiveness', 'xAppId', xAppId)
            // verify required parameter 'xAppSignature' is not null or undefined
            assertParamExists('updateRoleActiveness', 'xAppSignature', xAppSignature)
            // verify required parameter 'xAppDate' is not null or undefined
            assertParamExists('updateRoleActiveness', 'xAppDate', xAppDate)
            // verify required parameter 'roleActivenessSaveRequest' is not null or undefined
            assertParamExists('updateRoleActiveness', 'roleActivenessSaveRequest', roleActivenessSaveRequest)
            const localVarPath = `/api/v1/game/role-activeness`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'POST', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;



            localVarHeaderParameter['Content-Type'] = 'application/json';

            if (xAppId != null) {
                localVarHeaderParameter['X-App-Id'] = String(xAppId);
            }
            if (xAppSignature != null) {
                localVarHeaderParameter['X-App-Signature'] = String(xAppSignature);
            }
            if (xAppDate != null) {
                localVarHeaderParameter['X-App-Date'] = String(xAppDate);
            }
            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };
            localVarRequestOptions.data = serializeDataIfNeeded(roleActivenessSaveRequest, localVarRequestOptions, configuration)

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
    }
};

/**
 * RoleActivenessGameApi - functional programming interface
 * @export
 */
export const RoleActivenessGameApiFp = function (configuration?: Configuration) {
    const localVarAxiosParamCreator = RoleActivenessGameApiAxiosParamCreator(configuration)
    return {
        /**
         * 
         * @summary 更新角色每日活跃度
         * @param {string} xAppId 应用ID
         * @param {string} xAppSignature 应用签名
         * @param {string} xAppDate 应用时间戳
         * @param {RoleActivenessSaveRequest} roleActivenessSaveRequest 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async updateRoleActiveness(xAppId: string, xAppSignature: string, xAppDate: string, roleActivenessSaveRequest: RoleActivenessSaveRequest, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<BaseResponseBoolean>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.updateRoleActiveness(xAppId, xAppSignature, xAppDate, roleActivenessSaveRequest, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['RoleActivenessGameApi.updateRoleActiveness']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
    }
};

/**
 * RoleActivenessGameApi - factory interface
 * @export
 */
export const RoleActivenessGameApiFactory = function (configuration?: Configuration, basePath?: string, axios?: AxiosInstance) {
    const localVarFp = RoleActivenessGameApiFp(configuration)
    return {
        /**
         * 
         * @summary 更新角色每日活跃度
         * @param {RoleActivenessGameApiUpdateRoleActivenessRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        updateRoleActiveness(requestParameters: RoleActivenessGameApiUpdateRoleActivenessRequest, options?: RawAxiosRequestConfig): AxiosPromise<BaseResponseBoolean> {
            return localVarFp.updateRoleActiveness(requestParameters.xAppId, requestParameters.xAppSignature, requestParameters.xAppDate, requestParameters.roleActivenessSaveRequest, options).then((request) => request(axios, basePath));
        },
    };
};

/**
 * Request parameters for updateRoleActiveness operation in RoleActivenessGameApi.
 * @export
 * @interface RoleActivenessGameApiUpdateRoleActivenessRequest
 */
export interface RoleActivenessGameApiUpdateRoleActivenessRequest {
    /**
     * 应用ID
     * @type {string}
     * @memberof RoleActivenessGameApiUpdateRoleActiveness
     */
    readonly xAppId: string

    /**
     * 应用签名
     * @type {string}
     * @memberof RoleActivenessGameApiUpdateRoleActiveness
     */
    readonly xAppSignature: string

    /**
     * 应用时间戳
     * @type {string}
     * @memberof RoleActivenessGameApiUpdateRoleActiveness
     */
    readonly xAppDate: string

    /**
     * 
     * @type {RoleActivenessSaveRequest}
     * @memberof RoleActivenessGameApiUpdateRoleActiveness
     */
    readonly roleActivenessSaveRequest: RoleActivenessSaveRequest
}

/**
 * RoleActivenessGameApi - object-oriented interface
 * @export
 * @class RoleActivenessGameApi
 * @extends {BaseAPI}
 */
export class RoleActivenessGameApi extends BaseAPI {
    /**
     * 
     * @summary 更新角色每日活跃度
     * @param {RoleActivenessGameApiUpdateRoleActivenessRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof RoleActivenessGameApi
     */
    public updateRoleActiveness(requestParameters: RoleActivenessGameApiUpdateRoleActivenessRequest, options?: RawAxiosRequestConfig) {
        return RoleActivenessGameApiFp(this.configuration).updateRoleActiveness(requestParameters.xAppId, requestParameters.xAppSignature, requestParameters.xAppDate, requestParameters.roleActivenessSaveRequest, options).then((request) => request(this.axios, this.basePath));
    }
}



/**
 * RoleInviteMpApi - axios parameter creator
 * @export
 */
export const RoleInviteMpApiAxiosParamCreator = function (configuration?: Configuration) {
    return {
        /**
         * 
         * @summary 判断邀请者是否已经完成了人拉人任务，不需要助力
         * @param {string} inviter 邀请者角色id
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        checkInviteFinishMp: async (inviter: string, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'inviter' is not null or undefined
            assertParamExists('checkInviteFinishMp', 'inviter', inviter)
            const localVarPath = `/api/v1/mp/role-invite/inviter-check`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)

            if (inviter !== undefined) {
                localVarQueryParameter['inviter'] = inviter;
            }



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 创建角色邀请绑定关系
         * @param {RoleInviteRelationBindRequest} roleInviteRelationBindRequest 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        createBindRelationMp: async (roleInviteRelationBindRequest: RoleInviteRelationBindRequest, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'roleInviteRelationBindRequest' is not null or undefined
            assertParamExists('createBindRelationMp', 'roleInviteRelationBindRequest', roleInviteRelationBindRequest)
            const localVarPath = `/api/v1/mp/role-invite/bind`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'POST', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            localVarHeaderParameter['Content-Type'] = 'application/json';

            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };
            localVarRequestOptions.data = serializeDataIfNeeded(roleInviteRelationBindRequest, localVarRequestOptions, configuration)

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 查询当前用户作为邀请人的可领取和已领取的绑定关系列表
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        findRoleInviteRelationAvailableRewardsMp: async (options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            const localVarPath = `/api/v1/mp/role-invite/rewards`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 查询自己作为被邀请人的绑定关系
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        findRoleInviteRelationByHelperMp: async (options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            const localVarPath = `/api/v1/mp/role-invite/help-relation`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 领取指定奖励
         * @param {number} rewardIndex 奖励序号
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        receiveRoleInviteRelationRewardMp: async (rewardIndex: number, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'rewardIndex' is not null or undefined
            assertParamExists('receiveRoleInviteRelationRewardMp', 'rewardIndex', rewardIndex)
            const localVarPath = `/api/v1/mp/role-invite/receive/{rewardIndex}`
                .replace(`{${"rewardIndex"}}`, encodeURIComponent(String(rewardIndex)));
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 判断自己是否作为被邀请人已存在绑定关系
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        roleInviteRelationHelpCheckMp: async (options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            const localVarPath = `/api/v1/mp/role-invite/help-check`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
    }
};

/**
 * RoleInviteMpApi - functional programming interface
 * @export
 */
export const RoleInviteMpApiFp = function (configuration?: Configuration) {
    const localVarAxiosParamCreator = RoleInviteMpApiAxiosParamCreator(configuration)
    return {
        /**
         * 
         * @summary 判断邀请者是否已经完成了人拉人任务，不需要助力
         * @param {string} inviter 邀请者角色id
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async checkInviteFinishMp(inviter: string, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<boolean>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.checkInviteFinishMp(inviter, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['RoleInviteMpApi.checkInviteFinishMp']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 创建角色邀请绑定关系
         * @param {RoleInviteRelationBindRequest} roleInviteRelationBindRequest 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async createBindRelationMp(roleInviteRelationBindRequest: RoleInviteRelationBindRequest, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<CreateBindRelationResultVO>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.createBindRelationMp(roleInviteRelationBindRequest, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['RoleInviteMpApi.createBindRelationMp']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 查询当前用户作为邀请人的可领取和已领取的绑定关系列表
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async findRoleInviteRelationAvailableRewardsMp(options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<Array<RoleInviteRelation>>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.findRoleInviteRelationAvailableRewardsMp(options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['RoleInviteMpApi.findRoleInviteRelationAvailableRewardsMp']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 查询自己作为被邀请人的绑定关系
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async findRoleInviteRelationByHelperMp(options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<RoleInviteRelation>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.findRoleInviteRelationByHelperMp(options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['RoleInviteMpApi.findRoleInviteRelationByHelperMp']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 领取指定奖励
         * @param {number} rewardIndex 奖励序号
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async receiveRoleInviteRelationRewardMp(rewardIndex: number, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<boolean>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.receiveRoleInviteRelationRewardMp(rewardIndex, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['RoleInviteMpApi.receiveRoleInviteRelationRewardMp']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 判断自己是否作为被邀请人已存在绑定关系
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async roleInviteRelationHelpCheckMp(options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<boolean>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.roleInviteRelationHelpCheckMp(options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['RoleInviteMpApi.roleInviteRelationHelpCheckMp']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
    }
};

/**
 * RoleInviteMpApi - factory interface
 * @export
 */
export const RoleInviteMpApiFactory = function (configuration?: Configuration, basePath?: string, axios?: AxiosInstance) {
    const localVarFp = RoleInviteMpApiFp(configuration)
    return {
        /**
         * 
         * @summary 判断邀请者是否已经完成了人拉人任务，不需要助力
         * @param {RoleInviteMpApiCheckInviteFinishMpRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        checkInviteFinishMp(requestParameters: RoleInviteMpApiCheckInviteFinishMpRequest, options?: RawAxiosRequestConfig): AxiosPromise<boolean> {
            return localVarFp.checkInviteFinishMp(requestParameters.inviter, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 创建角色邀请绑定关系
         * @param {RoleInviteMpApiCreateBindRelationMpRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        createBindRelationMp(requestParameters: RoleInviteMpApiCreateBindRelationMpRequest, options?: RawAxiosRequestConfig): AxiosPromise<CreateBindRelationResultVO> {
            return localVarFp.createBindRelationMp(requestParameters.roleInviteRelationBindRequest, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 查询当前用户作为邀请人的可领取和已领取的绑定关系列表
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        findRoleInviteRelationAvailableRewardsMp(options?: RawAxiosRequestConfig): AxiosPromise<Array<RoleInviteRelation>> {
            return localVarFp.findRoleInviteRelationAvailableRewardsMp(options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 查询自己作为被邀请人的绑定关系
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        findRoleInviteRelationByHelperMp(options?: RawAxiosRequestConfig): AxiosPromise<RoleInviteRelation> {
            return localVarFp.findRoleInviteRelationByHelperMp(options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 领取指定奖励
         * @param {RoleInviteMpApiReceiveRoleInviteRelationRewardMpRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        receiveRoleInviteRelationRewardMp(requestParameters: RoleInviteMpApiReceiveRoleInviteRelationRewardMpRequest, options?: RawAxiosRequestConfig): AxiosPromise<boolean> {
            return localVarFp.receiveRoleInviteRelationRewardMp(requestParameters.rewardIndex, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 判断自己是否作为被邀请人已存在绑定关系
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        roleInviteRelationHelpCheckMp(options?: RawAxiosRequestConfig): AxiosPromise<boolean> {
            return localVarFp.roleInviteRelationHelpCheckMp(options).then((request) => request(axios, basePath));
        },
    };
};

/**
 * Request parameters for checkInviteFinishMp operation in RoleInviteMpApi.
 * @export
 * @interface RoleInviteMpApiCheckInviteFinishMpRequest
 */
export interface RoleInviteMpApiCheckInviteFinishMpRequest {
    /**
     * 邀请者角色id
     * @type {string}
     * @memberof RoleInviteMpApiCheckInviteFinishMp
     */
    readonly inviter: string
}

/**
 * Request parameters for createBindRelationMp operation in RoleInviteMpApi.
 * @export
 * @interface RoleInviteMpApiCreateBindRelationMpRequest
 */
export interface RoleInviteMpApiCreateBindRelationMpRequest {
    /**
     * 
     * @type {RoleInviteRelationBindRequest}
     * @memberof RoleInviteMpApiCreateBindRelationMp
     */
    readonly roleInviteRelationBindRequest: RoleInviteRelationBindRequest
}

/**
 * Request parameters for receiveRoleInviteRelationRewardMp operation in RoleInviteMpApi.
 * @export
 * @interface RoleInviteMpApiReceiveRoleInviteRelationRewardMpRequest
 */
export interface RoleInviteMpApiReceiveRoleInviteRelationRewardMpRequest {
    /**
     * 奖励序号
     * @type {number}
     * @memberof RoleInviteMpApiReceiveRoleInviteRelationRewardMp
     */
    readonly rewardIndex: number
}

/**
 * RoleInviteMpApi - object-oriented interface
 * @export
 * @class RoleInviteMpApi
 * @extends {BaseAPI}
 */
export class RoleInviteMpApi extends BaseAPI {
    /**
     * 
     * @summary 判断邀请者是否已经完成了人拉人任务，不需要助力
     * @param {RoleInviteMpApiCheckInviteFinishMpRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof RoleInviteMpApi
     */
    public checkInviteFinishMp(requestParameters: RoleInviteMpApiCheckInviteFinishMpRequest, options?: RawAxiosRequestConfig) {
        return RoleInviteMpApiFp(this.configuration).checkInviteFinishMp(requestParameters.inviter, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 创建角色邀请绑定关系
     * @param {RoleInviteMpApiCreateBindRelationMpRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof RoleInviteMpApi
     */
    public createBindRelationMp(requestParameters: RoleInviteMpApiCreateBindRelationMpRequest, options?: RawAxiosRequestConfig) {
        return RoleInviteMpApiFp(this.configuration).createBindRelationMp(requestParameters.roleInviteRelationBindRequest, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 查询当前用户作为邀请人的可领取和已领取的绑定关系列表
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof RoleInviteMpApi
     */
    public findRoleInviteRelationAvailableRewardsMp(options?: RawAxiosRequestConfig) {
        return RoleInviteMpApiFp(this.configuration).findRoleInviteRelationAvailableRewardsMp(options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 查询自己作为被邀请人的绑定关系
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof RoleInviteMpApi
     */
    public findRoleInviteRelationByHelperMp(options?: RawAxiosRequestConfig) {
        return RoleInviteMpApiFp(this.configuration).findRoleInviteRelationByHelperMp(options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 领取指定奖励
     * @param {RoleInviteMpApiReceiveRoleInviteRelationRewardMpRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof RoleInviteMpApi
     */
    public receiveRoleInviteRelationRewardMp(requestParameters: RoleInviteMpApiReceiveRoleInviteRelationRewardMpRequest, options?: RawAxiosRequestConfig) {
        return RoleInviteMpApiFp(this.configuration).receiveRoleInviteRelationRewardMp(requestParameters.rewardIndex, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 判断自己是否作为被邀请人已存在绑定关系
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof RoleInviteMpApi
     */
    public roleInviteRelationHelpCheckMp(options?: RawAxiosRequestConfig) {
        return RoleInviteMpApiFp(this.configuration).roleInviteRelationHelpCheckMp(options).then((request) => request(this.axios, this.basePath));
    }
}



/**
 * RoleMpApi - axios parameter creator
 * @export
 */
export const RoleMpApiAxiosParamCreator = function (configuration?: Configuration) {
    return {
        /**
         * 
         * @summary 获取指定角色的基本信息
         * @param {string} roleId 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getRoleBaseInfoByRoleIdMp: async (roleId: string, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'roleId' is not null or undefined
            assertParamExists('getRoleBaseInfoByRoleIdMp', 'roleId', roleId)
            const localVarPath = `/api/v1/mp/role/{roleId}/base-info`
                .replace(`{${"roleId"}}`, encodeURIComponent(String(roleId)));
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
    }
};

/**
 * RoleMpApi - functional programming interface
 * @export
 */
export const RoleMpApiFp = function (configuration?: Configuration) {
    const localVarAxiosParamCreator = RoleMpApiAxiosParamCreator(configuration)
    return {
        /**
         * 
         * @summary 获取指定角色的基本信息
         * @param {string} roleId 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async getRoleBaseInfoByRoleIdMp(roleId: string, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<RoleBaseInfoVO>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.getRoleBaseInfoByRoleIdMp(roleId, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['RoleMpApi.getRoleBaseInfoByRoleIdMp']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
    }
};

/**
 * RoleMpApi - factory interface
 * @export
 */
export const RoleMpApiFactory = function (configuration?: Configuration, basePath?: string, axios?: AxiosInstance) {
    const localVarFp = RoleMpApiFp(configuration)
    return {
        /**
         * 
         * @summary 获取指定角色的基本信息
         * @param {RoleMpApiGetRoleBaseInfoByRoleIdMpRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getRoleBaseInfoByRoleIdMp(requestParameters: RoleMpApiGetRoleBaseInfoByRoleIdMpRequest, options?: RawAxiosRequestConfig): AxiosPromise<RoleBaseInfoVO> {
            return localVarFp.getRoleBaseInfoByRoleIdMp(requestParameters.roleId, options).then((request) => request(axios, basePath));
        },
    };
};

/**
 * Request parameters for getRoleBaseInfoByRoleIdMp operation in RoleMpApi.
 * @export
 * @interface RoleMpApiGetRoleBaseInfoByRoleIdMpRequest
 */
export interface RoleMpApiGetRoleBaseInfoByRoleIdMpRequest {
    /**
     * 
     * @type {string}
     * @memberof RoleMpApiGetRoleBaseInfoByRoleIdMp
     */
    readonly roleId: string
}

/**
 * RoleMpApi - object-oriented interface
 * @export
 * @class RoleMpApi
 * @extends {BaseAPI}
 */
export class RoleMpApi extends BaseAPI {
    /**
     * 
     * @summary 获取指定角色的基本信息
     * @param {RoleMpApiGetRoleBaseInfoByRoleIdMpRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof RoleMpApi
     */
    public getRoleBaseInfoByRoleIdMp(requestParameters: RoleMpApiGetRoleBaseInfoByRoleIdMpRequest, options?: RawAxiosRequestConfig) {
        return RoleMpApiFp(this.configuration).getRoleBaseInfoByRoleIdMp(requestParameters.roleId, options).then((request) => request(this.axios, this.basePath));
    }
}



/**
 * ScoreExpireNotifyTaskMpApi - axios parameter creator
 * @export
 */
export const ScoreExpireNotifyTaskMpApiAxiosParamCreator = function (configuration?: Configuration) {
    return {
        /**
         * 
         * @summary 查询当前用户是否已订阅今年的积分到期通知
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        checkScoreExpireNotifyTaskMp: async (options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            const localVarPath = `/api/v1/mp/score-expire-notify-task/check`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 创建年度积分到期通知任务
         * @param {NotifyTaskCreateRequest} notifyTaskCreateRequest 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        createScoreExpireNotifyTaskMp: async (notifyTaskCreateRequest: NotifyTaskCreateRequest, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'notifyTaskCreateRequest' is not null or undefined
            assertParamExists('createScoreExpireNotifyTaskMp', 'notifyTaskCreateRequest', notifyTaskCreateRequest)
            const localVarPath = `/api/v1/mp/score-expire-notify-task`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'POST', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            localVarHeaderParameter['Content-Type'] = 'application/json';

            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };
            localVarRequestOptions.data = serializeDataIfNeeded(notifyTaskCreateRequest, localVarRequestOptions, configuration)

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
    }
};

/**
 * ScoreExpireNotifyTaskMpApi - functional programming interface
 * @export
 */
export const ScoreExpireNotifyTaskMpApiFp = function (configuration?: Configuration) {
    const localVarAxiosParamCreator = ScoreExpireNotifyTaskMpApiAxiosParamCreator(configuration)
    return {
        /**
         * 
         * @summary 查询当前用户是否已订阅今年的积分到期通知
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async checkScoreExpireNotifyTaskMp(options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<boolean>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.checkScoreExpireNotifyTaskMp(options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['ScoreExpireNotifyTaskMpApi.checkScoreExpireNotifyTaskMp']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 创建年度积分到期通知任务
         * @param {NotifyTaskCreateRequest} notifyTaskCreateRequest 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async createScoreExpireNotifyTaskMp(notifyTaskCreateRequest: NotifyTaskCreateRequest, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<NotifyTask>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.createScoreExpireNotifyTaskMp(notifyTaskCreateRequest, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['ScoreExpireNotifyTaskMpApi.createScoreExpireNotifyTaskMp']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
    }
};

/**
 * ScoreExpireNotifyTaskMpApi - factory interface
 * @export
 */
export const ScoreExpireNotifyTaskMpApiFactory = function (configuration?: Configuration, basePath?: string, axios?: AxiosInstance) {
    const localVarFp = ScoreExpireNotifyTaskMpApiFp(configuration)
    return {
        /**
         * 
         * @summary 查询当前用户是否已订阅今年的积分到期通知
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        checkScoreExpireNotifyTaskMp(options?: RawAxiosRequestConfig): AxiosPromise<boolean> {
            return localVarFp.checkScoreExpireNotifyTaskMp(options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 创建年度积分到期通知任务
         * @param {ScoreExpireNotifyTaskMpApiCreateScoreExpireNotifyTaskMpRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        createScoreExpireNotifyTaskMp(requestParameters: ScoreExpireNotifyTaskMpApiCreateScoreExpireNotifyTaskMpRequest, options?: RawAxiosRequestConfig): AxiosPromise<NotifyTask> {
            return localVarFp.createScoreExpireNotifyTaskMp(requestParameters.notifyTaskCreateRequest, options).then((request) => request(axios, basePath));
        },
    };
};

/**
 * Request parameters for createScoreExpireNotifyTaskMp operation in ScoreExpireNotifyTaskMpApi.
 * @export
 * @interface ScoreExpireNotifyTaskMpApiCreateScoreExpireNotifyTaskMpRequest
 */
export interface ScoreExpireNotifyTaskMpApiCreateScoreExpireNotifyTaskMpRequest {
    /**
     * 
     * @type {NotifyTaskCreateRequest}
     * @memberof ScoreExpireNotifyTaskMpApiCreateScoreExpireNotifyTaskMp
     */
    readonly notifyTaskCreateRequest: NotifyTaskCreateRequest
}

/**
 * ScoreExpireNotifyTaskMpApi - object-oriented interface
 * @export
 * @class ScoreExpireNotifyTaskMpApi
 * @extends {BaseAPI}
 */
export class ScoreExpireNotifyTaskMpApi extends BaseAPI {
    /**
     * 
     * @summary 查询当前用户是否已订阅今年的积分到期通知
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof ScoreExpireNotifyTaskMpApi
     */
    public checkScoreExpireNotifyTaskMp(options?: RawAxiosRequestConfig) {
        return ScoreExpireNotifyTaskMpApiFp(this.configuration).checkScoreExpireNotifyTaskMp(options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 创建年度积分到期通知任务
     * @param {ScoreExpireNotifyTaskMpApiCreateScoreExpireNotifyTaskMpRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof ScoreExpireNotifyTaskMpApi
     */
    public createScoreExpireNotifyTaskMp(requestParameters: ScoreExpireNotifyTaskMpApiCreateScoreExpireNotifyTaskMpRequest, options?: RawAxiosRequestConfig) {
        return ScoreExpireNotifyTaskMpApiFp(this.configuration).createScoreExpireNotifyTaskMp(requestParameters.notifyTaskCreateRequest, options).then((request) => request(this.axios, this.basePath));
    }
}



/**
 * StaticsApi - axios parameter creator
 * @export
 */
export const StaticsApiAxiosParamCreator = function (configuration?: Configuration) {
    return {
        /**
         * 
         * @summary 获取指定 key 静态信息。
         * @param {string} key 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getItem: async (key: string, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'key' is not null or undefined
            assertParamExists('getItem', 'key', key)
            const localVarPath = `/api/v1/statics/{key}`
                .replace(`{${"key"}}`, encodeURIComponent(String(key)));
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 获取所有静态信息。
         * @param {Set<string>} [name] 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getItems: async (name?: Set<string>, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            const localVarPath = `/api/v1/statics`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)

            if (name) {
                localVarQueryParameter['name'] = Array.from(name);
            }



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 获取当前系统时间。
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getTimeStamp: async (options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            const localVarPath = `/api/v1/statics/time-stamp`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
    }
};

/**
 * StaticsApi - functional programming interface
 * @export
 */
export const StaticsApiFp = function (configuration?: Configuration) {
    const localVarAxiosParamCreator = StaticsApiAxiosParamCreator(configuration)
    return {
        /**
         * 
         * @summary 获取指定 key 静态信息。
         * @param {string} key 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async getItem(key: string, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<object>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.getItem(key, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['StaticsApi.getItem']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 获取所有静态信息。
         * @param {Set<string>} [name] 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async getItems(name?: Set<string>, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<{ [key: string]: object; }>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.getItems(name, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['StaticsApi.getItems']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 获取当前系统时间。
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async getTimeStamp(options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<string>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.getTimeStamp(options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['StaticsApi.getTimeStamp']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
    }
};

/**
 * StaticsApi - factory interface
 * @export
 */
export const StaticsApiFactory = function (configuration?: Configuration, basePath?: string, axios?: AxiosInstance) {
    const localVarFp = StaticsApiFp(configuration)
    return {
        /**
         * 
         * @summary 获取指定 key 静态信息。
         * @param {StaticsApiGetItemRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getItem(requestParameters: StaticsApiGetItemRequest, options?: RawAxiosRequestConfig): AxiosPromise<object> {
            return localVarFp.getItem(requestParameters.key, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 获取所有静态信息。
         * @param {StaticsApiGetItemsRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getItems(requestParameters: StaticsApiGetItemsRequest = {}, options?: RawAxiosRequestConfig): AxiosPromise<{ [key: string]: object; }> {
            return localVarFp.getItems(requestParameters.name, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 获取当前系统时间。
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getTimeStamp(options?: RawAxiosRequestConfig): AxiosPromise<string> {
            return localVarFp.getTimeStamp(options).then((request) => request(axios, basePath));
        },
    };
};

/**
 * Request parameters for getItem operation in StaticsApi.
 * @export
 * @interface StaticsApiGetItemRequest
 */
export interface StaticsApiGetItemRequest {
    /**
     * 
     * @type {string}
     * @memberof StaticsApiGetItem
     */
    readonly key: string
}

/**
 * Request parameters for getItems operation in StaticsApi.
 * @export
 * @interface StaticsApiGetItemsRequest
 */
export interface StaticsApiGetItemsRequest {
    /**
     * 
     * @type {Set<string>}
     * @memberof StaticsApiGetItems
     */
    readonly name?: Set<string>
}

/**
 * StaticsApi - object-oriented interface
 * @export
 * @class StaticsApi
 * @extends {BaseAPI}
 */
export class StaticsApi extends BaseAPI {
    /**
     * 
     * @summary 获取指定 key 静态信息。
     * @param {StaticsApiGetItemRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof StaticsApi
     */
    public getItem(requestParameters: StaticsApiGetItemRequest, options?: RawAxiosRequestConfig) {
        return StaticsApiFp(this.configuration).getItem(requestParameters.key, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 获取所有静态信息。
     * @param {StaticsApiGetItemsRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof StaticsApi
     */
    public getItems(requestParameters: StaticsApiGetItemsRequest = {}, options?: RawAxiosRequestConfig) {
        return StaticsApiFp(this.configuration).getItems(requestParameters.name, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 获取当前系统时间。
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof StaticsApi
     */
    public getTimeStamp(options?: RawAxiosRequestConfig) {
        return StaticsApiFp(this.configuration).getTimeStamp(options).then((request) => request(this.axios, this.basePath));
    }
}



/**
 * TagQAApi - axios parameter creator
 * @export
 */
export const TagQAApiAxiosParamCreator = function (configuration?: Configuration) {
    return {
        /**
         * 
         * @summary 设置指定用户的某个tag的mock数据。
         * @param {string} tagId 
         * @param {string} userId 
         * @param {object} body 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        addTagsMock: async (tagId: string, userId: string, body: object, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'tagId' is not null or undefined
            assertParamExists('addTagsMock', 'tagId', tagId)
            // verify required parameter 'userId' is not null or undefined
            assertParamExists('addTagsMock', 'userId', userId)
            // verify required parameter 'body' is not null or undefined
            assertParamExists('addTagsMock', 'body', body)
            const localVarPath = `/api/v1/qa/tags/mock`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'POST', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)

            if (tagId !== undefined) {
                localVarQueryParameter['tagId'] = tagId;
            }

            if (userId !== undefined) {
                localVarQueryParameter['userId'] = userId;
            }



            localVarHeaderParameter['Content-Type'] = 'application/json';

            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };
            localVarRequestOptions.data = serializeDataIfNeeded(body, localVarRequestOptions, configuration)

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 删除指定用户的某个tag的mock数据。
         * @param {string} tagId 
         * @param {string} userId 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        deleteTagsMock: async (tagId: string, userId: string, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'tagId' is not null or undefined
            assertParamExists('deleteTagsMock', 'tagId', tagId)
            // verify required parameter 'userId' is not null or undefined
            assertParamExists('deleteTagsMock', 'userId', userId)
            const localVarPath = `/api/v1/qa/tags/mock`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'DELETE', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)

            if (tagId !== undefined) {
                localVarQueryParameter['tagId'] = tagId;
            }

            if (userId !== undefined) {
                localVarQueryParameter['userId'] = userId;
            }



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 获取所有的tags的mock数据。
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getTagsMock: async (options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            const localVarPath = `/api/v1/qa/tags/mock`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
    }
};

/**
 * TagQAApi - functional programming interface
 * @export
 */
export const TagQAApiFp = function (configuration?: Configuration) {
    const localVarAxiosParamCreator = TagQAApiAxiosParamCreator(configuration)
    return {
        /**
         * 
         * @summary 设置指定用户的某个tag的mock数据。
         * @param {string} tagId 
         * @param {string} userId 
         * @param {object} body 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async addTagsMock(tagId: string, userId: string, body: object, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<void>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.addTagsMock(tagId, userId, body, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['TagQAApi.addTagsMock']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 删除指定用户的某个tag的mock数据。
         * @param {string} tagId 
         * @param {string} userId 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async deleteTagsMock(tagId: string, userId: string, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<void>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.deleteTagsMock(tagId, userId, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['TagQAApi.deleteTagsMock']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 获取所有的tags的mock数据。
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async getTagsMock(options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<{ [key: string]: { [key: string]: object; }; }>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.getTagsMock(options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['TagQAApi.getTagsMock']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
    }
};

/**
 * TagQAApi - factory interface
 * @export
 */
export const TagQAApiFactory = function (configuration?: Configuration, basePath?: string, axios?: AxiosInstance) {
    const localVarFp = TagQAApiFp(configuration)
    return {
        /**
         * 
         * @summary 设置指定用户的某个tag的mock数据。
         * @param {TagQAApiAddTagsMockRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        addTagsMock(requestParameters: TagQAApiAddTagsMockRequest, options?: RawAxiosRequestConfig): AxiosPromise<void> {
            return localVarFp.addTagsMock(requestParameters.tagId, requestParameters.userId, requestParameters.body, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 删除指定用户的某个tag的mock数据。
         * @param {TagQAApiDeleteTagsMockRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        deleteTagsMock(requestParameters: TagQAApiDeleteTagsMockRequest, options?: RawAxiosRequestConfig): AxiosPromise<void> {
            return localVarFp.deleteTagsMock(requestParameters.tagId, requestParameters.userId, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 获取所有的tags的mock数据。
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getTagsMock(options?: RawAxiosRequestConfig): AxiosPromise<{ [key: string]: { [key: string]: object; }; }> {
            return localVarFp.getTagsMock(options).then((request) => request(axios, basePath));
        },
    };
};

/**
 * Request parameters for addTagsMock operation in TagQAApi.
 * @export
 * @interface TagQAApiAddTagsMockRequest
 */
export interface TagQAApiAddTagsMockRequest {
    /**
     * 
     * @type {string}
     * @memberof TagQAApiAddTagsMock
     */
    readonly tagId: string

    /**
     * 
     * @type {string}
     * @memberof TagQAApiAddTagsMock
     */
    readonly userId: string

    /**
     * 
     * @type {object}
     * @memberof TagQAApiAddTagsMock
     */
    readonly body: object
}

/**
 * Request parameters for deleteTagsMock operation in TagQAApi.
 * @export
 * @interface TagQAApiDeleteTagsMockRequest
 */
export interface TagQAApiDeleteTagsMockRequest {
    /**
     * 
     * @type {string}
     * @memberof TagQAApiDeleteTagsMock
     */
    readonly tagId: string

    /**
     * 
     * @type {string}
     * @memberof TagQAApiDeleteTagsMock
     */
    readonly userId: string
}

/**
 * TagQAApi - object-oriented interface
 * @export
 * @class TagQAApi
 * @extends {BaseAPI}
 */
export class TagQAApi extends BaseAPI {
    /**
     * 
     * @summary 设置指定用户的某个tag的mock数据。
     * @param {TagQAApiAddTagsMockRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof TagQAApi
     */
    public addTagsMock(requestParameters: TagQAApiAddTagsMockRequest, options?: RawAxiosRequestConfig) {
        return TagQAApiFp(this.configuration).addTagsMock(requestParameters.tagId, requestParameters.userId, requestParameters.body, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 删除指定用户的某个tag的mock数据。
     * @param {TagQAApiDeleteTagsMockRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof TagQAApi
     */
    public deleteTagsMock(requestParameters: TagQAApiDeleteTagsMockRequest, options?: RawAxiosRequestConfig) {
        return TagQAApiFp(this.configuration).deleteTagsMock(requestParameters.tagId, requestParameters.userId, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 获取所有的tags的mock数据。
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof TagQAApi
     */
    public getTagsMock(options?: RawAxiosRequestConfig) {
        return TagQAApiFp(this.configuration).getTagsMock(options).then((request) => request(this.axios, this.basePath));
    }
}



/**
 * TagsApi - axios parameter creator
 * @export
 */
export const TagsApiAxiosParamCreator = function (configuration?: Configuration) {
    return {
        /**
         * 
         * @summary 获取用户条件标签列表。
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getTags: async (options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            const localVarPath = `/api/v1/user-tags`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
    }
};

/**
 * TagsApi - functional programming interface
 * @export
 */
export const TagsApiFp = function (configuration?: Configuration) {
    const localVarAxiosParamCreator = TagsApiAxiosParamCreator(configuration)
    return {
        /**
         * 
         * @summary 获取用户条件标签列表。
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async getTags(options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<Array<TagInfo>>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.getTags(options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['TagsApi.getTags']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
    }
};

/**
 * TagsApi - factory interface
 * @export
 */
export const TagsApiFactory = function (configuration?: Configuration, basePath?: string, axios?: AxiosInstance) {
    const localVarFp = TagsApiFp(configuration)
    return {
        /**
         * 
         * @summary 获取用户条件标签列表。
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getTags(options?: RawAxiosRequestConfig): AxiosPromise<Array<TagInfo>> {
            return localVarFp.getTags(options).then((request) => request(axios, basePath));
        },
    };
};

/**
 * TagsApi - object-oriented interface
 * @export
 * @class TagsApi
 * @extends {BaseAPI}
 */
export class TagsApi extends BaseAPI {
    /**
     * 
     * @summary 获取用户条件标签列表。
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof TagsApi
     */
    public getTags(options?: RawAxiosRequestConfig) {
        return TagsApiFp(this.configuration).getTags(options).then((request) => request(this.axios, this.basePath));
    }
}



/**
 * UDataApi - axios parameter creator
 * @export
 */
export const UDataApiAxiosParamCreator = function (configuration?: Configuration) {
    return {
        /**
         * 
         * @summary 记录点击事件
         * @param {string} page 页面
         * @param {string} btn 按钮
         * @param {string} [sharer] 分享者ID
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        click: async (page: string, btn: string, sharer?: string, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'page' is not null or undefined
            assertParamExists('click', 'page', page)
            // verify required parameter 'btn' is not null or undefined
            assertParamExists('click', 'btn', btn)
            const localVarPath = `/api/v1/ntes-udata/events/click`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'POST', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)

            if (sharer !== undefined) {
                localVarQueryParameter['sharer'] = sharer;
            }

            if (page !== undefined) {
                localVarQueryParameter['page'] = page;
            }

            if (btn !== undefined) {
                localVarQueryParameter['btn'] = btn;
            }



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 记录操作事件
         * @param {string} type 操作类型
         * @param {string} [sharer] 分享者ID
         * @param {string} [page] 页面
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        operation: async (type: string, sharer?: string, page?: string, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'type' is not null or undefined
            assertParamExists('operation', 'type', type)
            const localVarPath = `/api/v1/ntes-udata/events/operation`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'POST', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)

            if (sharer !== undefined) {
                localVarQueryParameter['sharer'] = sharer;
            }

            if (page !== undefined) {
                localVarQueryParameter['page'] = page;
            }

            if (type !== undefined) {
                localVarQueryParameter['type'] = type;
            }



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 记录分享事件
         * @param {string} [sharer] 分享者ID
         * @param {string} [page] 页面
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        share: async (sharer?: string, page?: string, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            const localVarPath = `/api/v1/ntes-udata/events/share`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'POST', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)

            if (sharer !== undefined) {
                localVarQueryParameter['sharer'] = sharer;
            }

            if (page !== undefined) {
                localVarQueryParameter['page'] = page;
            }



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 记录浏览事件
         * @param {string} [sharer] 分享者ID
         * @param {string} [page] 页面
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        view: async (sharer?: string, page?: string, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            const localVarPath = `/api/v1/ntes-udata/events/view`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'POST', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)

            if (sharer !== undefined) {
                localVarQueryParameter['sharer'] = sharer;
            }

            if (page !== undefined) {
                localVarQueryParameter['page'] = page;
            }



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
    }
};

/**
 * UDataApi - functional programming interface
 * @export
 */
export const UDataApiFp = function (configuration?: Configuration) {
    const localVarAxiosParamCreator = UDataApiAxiosParamCreator(configuration)
    return {
        /**
         * 
         * @summary 记录点击事件
         * @param {string} page 页面
         * @param {string} btn 按钮
         * @param {string} [sharer] 分享者ID
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async click(page: string, btn: string, sharer?: string, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<void>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.click(page, btn, sharer, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['UDataApi.click']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 记录操作事件
         * @param {string} type 操作类型
         * @param {string} [sharer] 分享者ID
         * @param {string} [page] 页面
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async operation(type: string, sharer?: string, page?: string, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<void>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.operation(type, sharer, page, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['UDataApi.operation']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 记录分享事件
         * @param {string} [sharer] 分享者ID
         * @param {string} [page] 页面
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async share(sharer?: string, page?: string, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<void>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.share(sharer, page, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['UDataApi.share']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 记录浏览事件
         * @param {string} [sharer] 分享者ID
         * @param {string} [page] 页面
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async view(sharer?: string, page?: string, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<void>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.view(sharer, page, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['UDataApi.view']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
    }
};

/**
 * UDataApi - factory interface
 * @export
 */
export const UDataApiFactory = function (configuration?: Configuration, basePath?: string, axios?: AxiosInstance) {
    const localVarFp = UDataApiFp(configuration)
    return {
        /**
         * 
         * @summary 记录点击事件
         * @param {UDataApiClickRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        click(requestParameters: UDataApiClickRequest, options?: RawAxiosRequestConfig): AxiosPromise<void> {
            return localVarFp.click(requestParameters.page, requestParameters.btn, requestParameters.sharer, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 记录操作事件
         * @param {UDataApiOperationRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        operation(requestParameters: UDataApiOperationRequest, options?: RawAxiosRequestConfig): AxiosPromise<void> {
            return localVarFp.operation(requestParameters.type, requestParameters.sharer, requestParameters.page, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 记录分享事件
         * @param {UDataApiShareRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        share(requestParameters: UDataApiShareRequest = {}, options?: RawAxiosRequestConfig): AxiosPromise<void> {
            return localVarFp.share(requestParameters.sharer, requestParameters.page, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 记录浏览事件
         * @param {UDataApiViewRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        view(requestParameters: UDataApiViewRequest = {}, options?: RawAxiosRequestConfig): AxiosPromise<void> {
            return localVarFp.view(requestParameters.sharer, requestParameters.page, options).then((request) => request(axios, basePath));
        },
    };
};

/**
 * Request parameters for click operation in UDataApi.
 * @export
 * @interface UDataApiClickRequest
 */
export interface UDataApiClickRequest {
    /**
     * 页面
     * @type {string}
     * @memberof UDataApiClick
     */
    readonly page: string

    /**
     * 按钮
     * @type {string}
     * @memberof UDataApiClick
     */
    readonly btn: string

    /**
     * 分享者ID
     * @type {string}
     * @memberof UDataApiClick
     */
    readonly sharer?: string
}

/**
 * Request parameters for operation operation in UDataApi.
 * @export
 * @interface UDataApiOperationRequest
 */
export interface UDataApiOperationRequest {
    /**
     * 操作类型
     * @type {string}
     * @memberof UDataApiOperation
     */
    readonly type: string

    /**
     * 分享者ID
     * @type {string}
     * @memberof UDataApiOperation
     */
    readonly sharer?: string

    /**
     * 页面
     * @type {string}
     * @memberof UDataApiOperation
     */
    readonly page?: string
}

/**
 * Request parameters for share operation in UDataApi.
 * @export
 * @interface UDataApiShareRequest
 */
export interface UDataApiShareRequest {
    /**
     * 分享者ID
     * @type {string}
     * @memberof UDataApiShare
     */
    readonly sharer?: string

    /**
     * 页面
     * @type {string}
     * @memberof UDataApiShare
     */
    readonly page?: string
}

/**
 * Request parameters for view operation in UDataApi.
 * @export
 * @interface UDataApiViewRequest
 */
export interface UDataApiViewRequest {
    /**
     * 分享者ID
     * @type {string}
     * @memberof UDataApiView
     */
    readonly sharer?: string

    /**
     * 页面
     * @type {string}
     * @memberof UDataApiView
     */
    readonly page?: string
}

/**
 * UDataApi - object-oriented interface
 * @export
 * @class UDataApi
 * @extends {BaseAPI}
 */
export class UDataApi extends BaseAPI {
    /**
     * 
     * @summary 记录点击事件
     * @param {UDataApiClickRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof UDataApi
     */
    public click(requestParameters: UDataApiClickRequest, options?: RawAxiosRequestConfig) {
        return UDataApiFp(this.configuration).click(requestParameters.page, requestParameters.btn, requestParameters.sharer, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 记录操作事件
     * @param {UDataApiOperationRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof UDataApi
     */
    public operation(requestParameters: UDataApiOperationRequest, options?: RawAxiosRequestConfig) {
        return UDataApiFp(this.configuration).operation(requestParameters.type, requestParameters.sharer, requestParameters.page, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 记录分享事件
     * @param {UDataApiShareRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof UDataApi
     */
    public share(requestParameters: UDataApiShareRequest = {}, options?: RawAxiosRequestConfig) {
        return UDataApiFp(this.configuration).share(requestParameters.sharer, requestParameters.page, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 记录浏览事件
     * @param {UDataApiViewRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof UDataApi
     */
    public view(requestParameters: UDataApiViewRequest = {}, options?: RawAxiosRequestConfig) {
        return UDataApiFp(this.configuration).view(requestParameters.sharer, requestParameters.page, options).then((request) => request(this.axios, this.basePath));
    }
}



/**
 * UrsQaTokensApi - axios parameter creator
 * @export
 */
export const UrsQaTokensApiAxiosParamCreator = function (configuration?: Configuration) {
    return {
        /**
         * 
         * @summary 管理员通过 SSN 创建访问凭据。
         * @param {string} ssn 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        createUrsToken1: async (ssn: string, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'ssn' is not null or undefined
            assertParamExists('createUrsToken1', 'ssn', ssn)
            const localVarPath = `/api/v1/urs/qa/token`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'POST', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)

            if (ssn !== undefined) {
                localVarQueryParameter['ssn'] = ssn;
            }



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 管理员通过 OpenId 进行绑定 SSN 或者创建用户。
         * @param {string} openId 
         * @param {string} ssn 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        createUrsTokenWithOpenId: async (openId: string, ssn: string, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'openId' is not null or undefined
            assertParamExists('createUrsTokenWithOpenId', 'openId', openId)
            // verify required parameter 'ssn' is not null or undefined
            assertParamExists('createUrsTokenWithOpenId', 'ssn', ssn)
            const localVarPath = `/api/v1/urs/qa/token-with-open-id`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'POST', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)

            if (openId !== undefined) {
                localVarQueryParameter['openId'] = openId;
            }

            if (ssn !== undefined) {
                localVarQueryParameter['ssn'] = ssn;
            }



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 管理员通过 SSN 新建绑定角色的用户并创建访问凭据
         * @param {CreateUrsTokenWithRoleRequest} createUrsTokenWithRoleRequest 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        createUrsTokenWithRole: async (createUrsTokenWithRoleRequest: CreateUrsTokenWithRoleRequest, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'createUrsTokenWithRoleRequest' is not null or undefined
            assertParamExists('createUrsTokenWithRole', 'createUrsTokenWithRoleRequest', createUrsTokenWithRoleRequest)
            const localVarPath = `/api/v1/urs/qa/token-with-role`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'POST', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            localVarHeaderParameter['Content-Type'] = 'application/json';

            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };
            localVarRequestOptions.data = serializeDataIfNeeded(createUrsTokenWithRoleRequest, localVarRequestOptions, configuration)

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
    }
};

/**
 * UrsQaTokensApi - functional programming interface
 * @export
 */
export const UrsQaTokensApiFp = function (configuration?: Configuration) {
    const localVarAxiosParamCreator = UrsQaTokensApiAxiosParamCreator(configuration)
    return {
        /**
         * 
         * @summary 管理员通过 SSN 创建访问凭据。
         * @param {string} ssn 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async createUrsToken1(ssn: string, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<string>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.createUrsToken1(ssn, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['UrsQaTokensApi.createUrsToken1']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 管理员通过 OpenId 进行绑定 SSN 或者创建用户。
         * @param {string} openId 
         * @param {string} ssn 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async createUrsTokenWithOpenId(openId: string, ssn: string, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<string>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.createUrsTokenWithOpenId(openId, ssn, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['UrsQaTokensApi.createUrsTokenWithOpenId']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 管理员通过 SSN 新建绑定角色的用户并创建访问凭据
         * @param {CreateUrsTokenWithRoleRequest} createUrsTokenWithRoleRequest 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async createUrsTokenWithRole(createUrsTokenWithRoleRequest: CreateUrsTokenWithRoleRequest, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<string>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.createUrsTokenWithRole(createUrsTokenWithRoleRequest, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['UrsQaTokensApi.createUrsTokenWithRole']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
    }
};

/**
 * UrsQaTokensApi - factory interface
 * @export
 */
export const UrsQaTokensApiFactory = function (configuration?: Configuration, basePath?: string, axios?: AxiosInstance) {
    const localVarFp = UrsQaTokensApiFp(configuration)
    return {
        /**
         * 
         * @summary 管理员通过 SSN 创建访问凭据。
         * @param {UrsQaTokensApiCreateUrsToken1Request} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        createUrsToken1(requestParameters: UrsQaTokensApiCreateUrsToken1Request, options?: RawAxiosRequestConfig): AxiosPromise<string> {
            return localVarFp.createUrsToken1(requestParameters.ssn, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 管理员通过 OpenId 进行绑定 SSN 或者创建用户。
         * @param {UrsQaTokensApiCreateUrsTokenWithOpenIdRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        createUrsTokenWithOpenId(requestParameters: UrsQaTokensApiCreateUrsTokenWithOpenIdRequest, options?: RawAxiosRequestConfig): AxiosPromise<string> {
            return localVarFp.createUrsTokenWithOpenId(requestParameters.openId, requestParameters.ssn, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 管理员通过 SSN 新建绑定角色的用户并创建访问凭据
         * @param {UrsQaTokensApiCreateUrsTokenWithRoleRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        createUrsTokenWithRole(requestParameters: UrsQaTokensApiCreateUrsTokenWithRoleRequest, options?: RawAxiosRequestConfig): AxiosPromise<string> {
            return localVarFp.createUrsTokenWithRole(requestParameters.createUrsTokenWithRoleRequest, options).then((request) => request(axios, basePath));
        },
    };
};

/**
 * Request parameters for createUrsToken1 operation in UrsQaTokensApi.
 * @export
 * @interface UrsQaTokensApiCreateUrsToken1Request
 */
export interface UrsQaTokensApiCreateUrsToken1Request {
    /**
     * 
     * @type {string}
     * @memberof UrsQaTokensApiCreateUrsToken1
     */
    readonly ssn: string
}

/**
 * Request parameters for createUrsTokenWithOpenId operation in UrsQaTokensApi.
 * @export
 * @interface UrsQaTokensApiCreateUrsTokenWithOpenIdRequest
 */
export interface UrsQaTokensApiCreateUrsTokenWithOpenIdRequest {
    /**
     * 
     * @type {string}
     * @memberof UrsQaTokensApiCreateUrsTokenWithOpenId
     */
    readonly openId: string

    /**
     * 
     * @type {string}
     * @memberof UrsQaTokensApiCreateUrsTokenWithOpenId
     */
    readonly ssn: string
}

/**
 * Request parameters for createUrsTokenWithRole operation in UrsQaTokensApi.
 * @export
 * @interface UrsQaTokensApiCreateUrsTokenWithRoleRequest
 */
export interface UrsQaTokensApiCreateUrsTokenWithRoleRequest {
    /**
     * 
     * @type {CreateUrsTokenWithRoleRequest}
     * @memberof UrsQaTokensApiCreateUrsTokenWithRole
     */
    readonly createUrsTokenWithRoleRequest: CreateUrsTokenWithRoleRequest
}

/**
 * UrsQaTokensApi - object-oriented interface
 * @export
 * @class UrsQaTokensApi
 * @extends {BaseAPI}
 */
export class UrsQaTokensApi extends BaseAPI {
    /**
     * 
     * @summary 管理员通过 SSN 创建访问凭据。
     * @param {UrsQaTokensApiCreateUrsToken1Request} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof UrsQaTokensApi
     */
    public createUrsToken1(requestParameters: UrsQaTokensApiCreateUrsToken1Request, options?: RawAxiosRequestConfig) {
        return UrsQaTokensApiFp(this.configuration).createUrsToken1(requestParameters.ssn, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 管理员通过 OpenId 进行绑定 SSN 或者创建用户。
     * @param {UrsQaTokensApiCreateUrsTokenWithOpenIdRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof UrsQaTokensApi
     */
    public createUrsTokenWithOpenId(requestParameters: UrsQaTokensApiCreateUrsTokenWithOpenIdRequest, options?: RawAxiosRequestConfig) {
        return UrsQaTokensApiFp(this.configuration).createUrsTokenWithOpenId(requestParameters.openId, requestParameters.ssn, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 管理员通过 SSN 新建绑定角色的用户并创建访问凭据
     * @param {UrsQaTokensApiCreateUrsTokenWithRoleRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof UrsQaTokensApi
     */
    public createUrsTokenWithRole(requestParameters: UrsQaTokensApiCreateUrsTokenWithRoleRequest, options?: RawAxiosRequestConfig) {
        return UrsQaTokensApiFp(this.configuration).createUrsTokenWithRole(requestParameters.createUrsTokenWithRoleRequest, options).then((request) => request(this.axios, this.basePath));
    }
}



/**
 * UrsTokensApi - axios parameter creator
 * @export
 */
export const UrsTokensApiAxiosParamCreator = function (configuration?: Configuration) {
    return {
        /**
         * 
         * @summary 通过 Cookie 绑定 SSN。
         * @param {string} [body] 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        bindUserSsn: async (body?: string, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            const localVarPath = `/api/v1/urs/binding`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'POST', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;



            localVarHeaderParameter['Content-Type'] = 'application/json';

            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };
            localVarRequestOptions.data = serializeDataIfNeeded(body, localVarRequestOptions, configuration)

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 通过 Cookie 绑定 SSN。（微信小程序用）
         * @param {string} body 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        bindUserSsnWechatMP: async (body: string, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'body' is not null or undefined
            assertParamExists('bindUserSsnWechatMP', 'body', body)
            const localVarPath = `/api/v1/urs/wechat-binding`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'POST', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;



            localVarHeaderParameter['Content-Type'] = 'application/json';

            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };
            localVarRequestOptions.data = serializeDataIfNeeded(body, localVarRequestOptions, configuration)

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 通过 Cookie 创建访问凭据。
         * @param {string} [body] 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        createUrsToken: async (body?: string, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            const localVarPath = `/api/v1/urs/token`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'POST', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;



            localVarHeaderParameter['Content-Type'] = 'application/json';

            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };
            localVarRequestOptions.data = serializeDataIfNeeded(body, localVarRequestOptions, configuration)

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 通过微信Urs Token创建访问凭据。
         * @param {string} body 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        createUrsWechatToken: async (body: string, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'body' is not null or undefined
            assertParamExists('createUrsWechatToken', 'body', body)
            const localVarPath = `/api/v1/urs/wechat-token`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'POST', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;



            localVarHeaderParameter['Content-Type'] = 'application/json';

            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };
            localVarRequestOptions.data = serializeDataIfNeeded(body, localVarRequestOptions, configuration)

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
    }
};

/**
 * UrsTokensApi - functional programming interface
 * @export
 */
export const UrsTokensApiFp = function (configuration?: Configuration) {
    const localVarAxiosParamCreator = UrsTokensApiAxiosParamCreator(configuration)
    return {
        /**
         * 
         * @summary 通过 Cookie 绑定 SSN。
         * @param {string} [body] 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async bindUserSsn(body?: string, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<User>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.bindUserSsn(body, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['UrsTokensApi.bindUserSsn']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 通过 Cookie 绑定 SSN。（微信小程序用）
         * @param {string} body 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async bindUserSsnWechatMP(body: string, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<User>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.bindUserSsnWechatMP(body, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['UrsTokensApi.bindUserSsnWechatMP']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 通过 Cookie 创建访问凭据。
         * @param {string} [body] 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async createUrsToken(body?: string, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<string>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.createUrsToken(body, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['UrsTokensApi.createUrsToken']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 通过微信Urs Token创建访问凭据。
         * @param {string} body 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async createUrsWechatToken(body: string, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<string>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.createUrsWechatToken(body, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['UrsTokensApi.createUrsWechatToken']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
    }
};

/**
 * UrsTokensApi - factory interface
 * @export
 */
export const UrsTokensApiFactory = function (configuration?: Configuration, basePath?: string, axios?: AxiosInstance) {
    const localVarFp = UrsTokensApiFp(configuration)
    return {
        /**
         * 
         * @summary 通过 Cookie 绑定 SSN。
         * @param {UrsTokensApiBindUserSsnRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        bindUserSsn(requestParameters: UrsTokensApiBindUserSsnRequest = {}, options?: RawAxiosRequestConfig): AxiosPromise<User> {
            return localVarFp.bindUserSsn(requestParameters.body, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 通过 Cookie 绑定 SSN。（微信小程序用）
         * @param {UrsTokensApiBindUserSsnWechatMPRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        bindUserSsnWechatMP(requestParameters: UrsTokensApiBindUserSsnWechatMPRequest, options?: RawAxiosRequestConfig): AxiosPromise<User> {
            return localVarFp.bindUserSsnWechatMP(requestParameters.body, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 通过 Cookie 创建访问凭据。
         * @param {UrsTokensApiCreateUrsTokenRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        createUrsToken(requestParameters: UrsTokensApiCreateUrsTokenRequest = {}, options?: RawAxiosRequestConfig): AxiosPromise<string> {
            return localVarFp.createUrsToken(requestParameters.body, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 通过微信Urs Token创建访问凭据。
         * @param {UrsTokensApiCreateUrsWechatTokenRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        createUrsWechatToken(requestParameters: UrsTokensApiCreateUrsWechatTokenRequest, options?: RawAxiosRequestConfig): AxiosPromise<string> {
            return localVarFp.createUrsWechatToken(requestParameters.body, options).then((request) => request(axios, basePath));
        },
    };
};

/**
 * Request parameters for bindUserSsn operation in UrsTokensApi.
 * @export
 * @interface UrsTokensApiBindUserSsnRequest
 */
export interface UrsTokensApiBindUserSsnRequest {
    /**
     * 
     * @type {string}
     * @memberof UrsTokensApiBindUserSsn
     */
    readonly body?: string
}

/**
 * Request parameters for bindUserSsnWechatMP operation in UrsTokensApi.
 * @export
 * @interface UrsTokensApiBindUserSsnWechatMPRequest
 */
export interface UrsTokensApiBindUserSsnWechatMPRequest {
    /**
     * 
     * @type {string}
     * @memberof UrsTokensApiBindUserSsnWechatMP
     */
    readonly body: string
}

/**
 * Request parameters for createUrsToken operation in UrsTokensApi.
 * @export
 * @interface UrsTokensApiCreateUrsTokenRequest
 */
export interface UrsTokensApiCreateUrsTokenRequest {
    /**
     * 
     * @type {string}
     * @memberof UrsTokensApiCreateUrsToken
     */
    readonly body?: string
}

/**
 * Request parameters for createUrsWechatToken operation in UrsTokensApi.
 * @export
 * @interface UrsTokensApiCreateUrsWechatTokenRequest
 */
export interface UrsTokensApiCreateUrsWechatTokenRequest {
    /**
     * 
     * @type {string}
     * @memberof UrsTokensApiCreateUrsWechatToken
     */
    readonly body: string
}

/**
 * UrsTokensApi - object-oriented interface
 * @export
 * @class UrsTokensApi
 * @extends {BaseAPI}
 */
export class UrsTokensApi extends BaseAPI {
    /**
     * 
     * @summary 通过 Cookie 绑定 SSN。
     * @param {UrsTokensApiBindUserSsnRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof UrsTokensApi
     */
    public bindUserSsn(requestParameters: UrsTokensApiBindUserSsnRequest = {}, options?: RawAxiosRequestConfig) {
        return UrsTokensApiFp(this.configuration).bindUserSsn(requestParameters.body, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 通过 Cookie 绑定 SSN。（微信小程序用）
     * @param {UrsTokensApiBindUserSsnWechatMPRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof UrsTokensApi
     */
    public bindUserSsnWechatMP(requestParameters: UrsTokensApiBindUserSsnWechatMPRequest, options?: RawAxiosRequestConfig) {
        return UrsTokensApiFp(this.configuration).bindUserSsnWechatMP(requestParameters.body, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 通过 Cookie 创建访问凭据。
     * @param {UrsTokensApiCreateUrsTokenRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof UrsTokensApi
     */
    public createUrsToken(requestParameters: UrsTokensApiCreateUrsTokenRequest = {}, options?: RawAxiosRequestConfig) {
        return UrsTokensApiFp(this.configuration).createUrsToken(requestParameters.body, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 通过微信Urs Token创建访问凭据。
     * @param {UrsTokensApiCreateUrsWechatTokenRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof UrsTokensApi
     */
    public createUrsWechatToken(requestParameters: UrsTokensApiCreateUrsWechatTokenRequest, options?: RawAxiosRequestConfig) {
        return UrsTokensApiFp(this.configuration).createUrsWechatToken(requestParameters.body, options).then((request) => request(this.axios, this.basePath));
    }
}



/**
 * UserLastActionMarkMpApi - axios parameter creator
 * @export
 */
export const UserLastActionMarkMpApiAxiosParamCreator = function (configuration?: Configuration) {
    return {
        /**
         * 
         * @summary 查询用户最后操作标记
         * @param {FindUserLastActionMarkByActionMpActionEnum} action 操作类型&lt;br&gt;枚举值说明：&lt;br&gt;BIND_ROLE: 绑定角色
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        findUserLastActionMarkByActionMp: async (action: FindUserLastActionMarkByActionMpActionEnum, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'action' is not null or undefined
            assertParamExists('findUserLastActionMarkByActionMp', 'action', action)
            const localVarPath = `/api/v1/mp/user-last-action-mark/{action}`
                .replace(`{${"action"}}`, encodeURIComponent(String(action)));
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 保存用户最后操作标记
         * @param {SaveUserLastActionMarkMpActionEnum} action 操作类型&lt;br&gt;枚举值说明：&lt;br&gt;BIND_ROLE: 绑定角色
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        saveUserLastActionMarkMp: async (action: SaveUserLastActionMarkMpActionEnum, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'action' is not null or undefined
            assertParamExists('saveUserLastActionMarkMp', 'action', action)
            const localVarPath = `/api/v1/mp/user-last-action-mark/{action}`
                .replace(`{${"action"}}`, encodeURIComponent(String(action)));
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'POST', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
    }
};

/**
 * UserLastActionMarkMpApi - functional programming interface
 * @export
 */
export const UserLastActionMarkMpApiFp = function (configuration?: Configuration) {
    const localVarAxiosParamCreator = UserLastActionMarkMpApiAxiosParamCreator(configuration)
    return {
        /**
         * 
         * @summary 查询用户最后操作标记
         * @param {FindUserLastActionMarkByActionMpActionEnum} action 操作类型&lt;br&gt;枚举值说明：&lt;br&gt;BIND_ROLE: 绑定角色
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async findUserLastActionMarkByActionMp(action: FindUserLastActionMarkByActionMpActionEnum, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<UserLastActionMark>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.findUserLastActionMarkByActionMp(action, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['UserLastActionMarkMpApi.findUserLastActionMarkByActionMp']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 保存用户最后操作标记
         * @param {SaveUserLastActionMarkMpActionEnum} action 操作类型&lt;br&gt;枚举值说明：&lt;br&gt;BIND_ROLE: 绑定角色
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async saveUserLastActionMarkMp(action: SaveUserLastActionMarkMpActionEnum, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<UserLastActionMark>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.saveUserLastActionMarkMp(action, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['UserLastActionMarkMpApi.saveUserLastActionMarkMp']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
    }
};

/**
 * UserLastActionMarkMpApi - factory interface
 * @export
 */
export const UserLastActionMarkMpApiFactory = function (configuration?: Configuration, basePath?: string, axios?: AxiosInstance) {
    const localVarFp = UserLastActionMarkMpApiFp(configuration)
    return {
        /**
         * 
         * @summary 查询用户最后操作标记
         * @param {UserLastActionMarkMpApiFindUserLastActionMarkByActionMpRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        findUserLastActionMarkByActionMp(requestParameters: UserLastActionMarkMpApiFindUserLastActionMarkByActionMpRequest, options?: RawAxiosRequestConfig): AxiosPromise<UserLastActionMark> {
            return localVarFp.findUserLastActionMarkByActionMp(requestParameters.action, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 保存用户最后操作标记
         * @param {UserLastActionMarkMpApiSaveUserLastActionMarkMpRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        saveUserLastActionMarkMp(requestParameters: UserLastActionMarkMpApiSaveUserLastActionMarkMpRequest, options?: RawAxiosRequestConfig): AxiosPromise<UserLastActionMark> {
            return localVarFp.saveUserLastActionMarkMp(requestParameters.action, options).then((request) => request(axios, basePath));
        },
    };
};

/**
 * Request parameters for findUserLastActionMarkByActionMp operation in UserLastActionMarkMpApi.
 * @export
 * @interface UserLastActionMarkMpApiFindUserLastActionMarkByActionMpRequest
 */
export interface UserLastActionMarkMpApiFindUserLastActionMarkByActionMpRequest {
    /**
     * 操作类型&lt;br&gt;枚举值说明：&lt;br&gt;BIND_ROLE: 绑定角色
     * @type {'BIND_ROLE'}
     * @memberof UserLastActionMarkMpApiFindUserLastActionMarkByActionMp
     */
    readonly action: FindUserLastActionMarkByActionMpActionEnum
}

/**
 * Request parameters for saveUserLastActionMarkMp operation in UserLastActionMarkMpApi.
 * @export
 * @interface UserLastActionMarkMpApiSaveUserLastActionMarkMpRequest
 */
export interface UserLastActionMarkMpApiSaveUserLastActionMarkMpRequest {
    /**
     * 操作类型&lt;br&gt;枚举值说明：&lt;br&gt;BIND_ROLE: 绑定角色
     * @type {'BIND_ROLE'}
     * @memberof UserLastActionMarkMpApiSaveUserLastActionMarkMp
     */
    readonly action: SaveUserLastActionMarkMpActionEnum
}

/**
 * UserLastActionMarkMpApi - object-oriented interface
 * @export
 * @class UserLastActionMarkMpApi
 * @extends {BaseAPI}
 */
export class UserLastActionMarkMpApi extends BaseAPI {
    /**
     * 
     * @summary 查询用户最后操作标记
     * @param {UserLastActionMarkMpApiFindUserLastActionMarkByActionMpRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof UserLastActionMarkMpApi
     */
    public findUserLastActionMarkByActionMp(requestParameters: UserLastActionMarkMpApiFindUserLastActionMarkByActionMpRequest, options?: RawAxiosRequestConfig) {
        return UserLastActionMarkMpApiFp(this.configuration).findUserLastActionMarkByActionMp(requestParameters.action, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 保存用户最后操作标记
     * @param {UserLastActionMarkMpApiSaveUserLastActionMarkMpRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof UserLastActionMarkMpApi
     */
    public saveUserLastActionMarkMp(requestParameters: UserLastActionMarkMpApiSaveUserLastActionMarkMpRequest, options?: RawAxiosRequestConfig) {
        return UserLastActionMarkMpApiFp(this.configuration).saveUserLastActionMarkMp(requestParameters.action, options).then((request) => request(this.axios, this.basePath));
    }
}

/**
 * @export
 */
export const FindUserLastActionMarkByActionMpActionEnum = {
    BindRole: 'BIND_ROLE'
} as const;
export type FindUserLastActionMarkByActionMpActionEnum = typeof FindUserLastActionMarkByActionMpActionEnum[keyof typeof FindUserLastActionMarkByActionMpActionEnum];
/**
 * @export
 */
export const SaveUserLastActionMarkMpActionEnum = {
    BindRole: 'BIND_ROLE'
} as const;
export type SaveUserLastActionMarkMpActionEnum = typeof SaveUserLastActionMarkMpActionEnum[keyof typeof SaveUserLastActionMarkMpActionEnum];


/**
 * UserPointApi - axios parameter creator
 * @export
 */
export const UserPointApiAxiosParamCreator = function (configuration?: Configuration) {
    return {
        /**
         * 
         * @summary 获取当前用户的数值变化记录总和。（管理员能传入参数 user 获取指定用户的数值变化记录。）一次最多查询 50 条。
         * @param {string} key 
         * @param {CountTypeEnum} [type] 
         * @param {string} [user] 
         * @param {string} [start] 
         * @param {string} [end] 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        count: async (key: string, type?: CountTypeEnum, user?: string, start?: string, end?: string, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'key' is not null or undefined
            assertParamExists('count', 'key', key)
            const localVarPath = `/api/v1/user-points/count/{key}`
                .replace(`{${"key"}}`, encodeURIComponent(String(key)));
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)

            if (type !== undefined) {
                localVarQueryParameter['type'] = type;
            }

            if (user !== undefined) {
                localVarQueryParameter['user'] = user;
            }

            if (start !== undefined) {
                localVarQueryParameter['start'] = (start as any instanceof Date) ?
                    (start as any).toISOString() :
                    start;
            }

            if (end !== undefined) {
                localVarQueryParameter['end'] = (end as any instanceof Date) ?
                    (end as any).toISOString() :
                    end;
            }



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 获取当前用户的数值变化记录。（管理员能传入参数 user 获取指定用户的数值变化记录。）一次最多查询 50 条。
         * @param {string} key 
         * @param {GetUserPointChangesTypeEnum} [type] 
         * @param {string} [user] 
         * @param {number} [offset] 
         * @param {number} [limit] 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getUserPointChanges: async (key: string, type?: GetUserPointChangesTypeEnum, user?: string, offset?: number, limit?: number, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'key' is not null or undefined
            assertParamExists('getUserPointChanges', 'key', key)
            const localVarPath = `/api/v1/user-points/changes/{key}`
                .replace(`{${"key"}}`, encodeURIComponent(String(key)));
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)

            if (type !== undefined) {
                localVarQueryParameter['type'] = type;
            }

            if (user !== undefined) {
                localVarQueryParameter['user'] = user;
            }

            if (offset !== undefined) {
                localVarQueryParameter['offset'] = offset;
            }

            if (limit !== undefined) {
                localVarQueryParameter['limit'] = limit;
            }



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 获取所有用户数值的 key 列表。
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getUserPointKeys1: async (options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            const localVarPath = `/api/v1/user-points/keys`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 获取当前用户指定 key 的用户数值。
         * @param {string} key 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getUserPointValue: async (key: string, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'key' is not null or undefined
            assertParamExists('getUserPointValue', 'key', key)
            const localVarPath = `/api/v1/user-points/values/{key}`
                .replace(`{${"key"}}`, encodeURIComponent(String(key)));
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
    }
};

/**
 * UserPointApi - functional programming interface
 * @export
 */
export const UserPointApiFp = function (configuration?: Configuration) {
    const localVarAxiosParamCreator = UserPointApiAxiosParamCreator(configuration)
    return {
        /**
         * 
         * @summary 获取当前用户的数值变化记录总和。（管理员能传入参数 user 获取指定用户的数值变化记录。）一次最多查询 50 条。
         * @param {string} key 
         * @param {CountTypeEnum} [type] 
         * @param {string} [user] 
         * @param {string} [start] 
         * @param {string} [end] 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async count(key: string, type?: CountTypeEnum, user?: string, start?: string, end?: string, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<ValueCount>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.count(key, type, user, start, end, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['UserPointApi.count']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 获取当前用户的数值变化记录。（管理员能传入参数 user 获取指定用户的数值变化记录。）一次最多查询 50 条。
         * @param {string} key 
         * @param {GetUserPointChangesTypeEnum} [type] 
         * @param {string} [user] 
         * @param {number} [offset] 
         * @param {number} [limit] 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async getUserPointChanges(key: string, type?: GetUserPointChangesTypeEnum, user?: string, offset?: number, limit?: number, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<Array<UserPointChangeRecord>>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.getUserPointChanges(key, type, user, offset, limit, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['UserPointApi.getUserPointChanges']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 获取所有用户数值的 key 列表。
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async getUserPointKeys1(options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<Array<UserPointKey>>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.getUserPointKeys1(options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['UserPointApi.getUserPointKeys1']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 获取当前用户指定 key 的用户数值。
         * @param {string} key 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async getUserPointValue(key: string, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<number>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.getUserPointValue(key, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['UserPointApi.getUserPointValue']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
    }
};

/**
 * UserPointApi - factory interface
 * @export
 */
export const UserPointApiFactory = function (configuration?: Configuration, basePath?: string, axios?: AxiosInstance) {
    const localVarFp = UserPointApiFp(configuration)
    return {
        /**
         * 
         * @summary 获取当前用户的数值变化记录总和。（管理员能传入参数 user 获取指定用户的数值变化记录。）一次最多查询 50 条。
         * @param {UserPointApiCountRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        count(requestParameters: UserPointApiCountRequest, options?: RawAxiosRequestConfig): AxiosPromise<ValueCount> {
            return localVarFp.count(requestParameters.key, requestParameters.type, requestParameters.user, requestParameters.start, requestParameters.end, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 获取当前用户的数值变化记录。（管理员能传入参数 user 获取指定用户的数值变化记录。）一次最多查询 50 条。
         * @param {UserPointApiGetUserPointChangesRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getUserPointChanges(requestParameters: UserPointApiGetUserPointChangesRequest, options?: RawAxiosRequestConfig): AxiosPromise<Array<UserPointChangeRecord>> {
            return localVarFp.getUserPointChanges(requestParameters.key, requestParameters.type, requestParameters.user, requestParameters.offset, requestParameters.limit, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 获取所有用户数值的 key 列表。
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getUserPointKeys1(options?: RawAxiosRequestConfig): AxiosPromise<Array<UserPointKey>> {
            return localVarFp.getUserPointKeys1(options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 获取当前用户指定 key 的用户数值。
         * @param {UserPointApiGetUserPointValueRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getUserPointValue(requestParameters: UserPointApiGetUserPointValueRequest, options?: RawAxiosRequestConfig): AxiosPromise<number> {
            return localVarFp.getUserPointValue(requestParameters.key, options).then((request) => request(axios, basePath));
        },
    };
};

/**
 * Request parameters for count operation in UserPointApi.
 * @export
 * @interface UserPointApiCountRequest
 */
export interface UserPointApiCountRequest {
    /**
     * 
     * @type {string}
     * @memberof UserPointApiCount
     */
    readonly key: string

    /**
     * 
     * @type {'INCREASE' | 'DECREASE'}
     * @memberof UserPointApiCount
     */
    readonly type?: CountTypeEnum

    /**
     * 
     * @type {string}
     * @memberof UserPointApiCount
     */
    readonly user?: string

    /**
     * 
     * @type {string}
     * @memberof UserPointApiCount
     */
    readonly start?: string

    /**
     * 
     * @type {string}
     * @memberof UserPointApiCount
     */
    readonly end?: string
}

/**
 * Request parameters for getUserPointChanges operation in UserPointApi.
 * @export
 * @interface UserPointApiGetUserPointChangesRequest
 */
export interface UserPointApiGetUserPointChangesRequest {
    /**
     * 
     * @type {string}
     * @memberof UserPointApiGetUserPointChanges
     */
    readonly key: string

    /**
     * 
     * @type {'INCREASE' | 'DECREASE'}
     * @memberof UserPointApiGetUserPointChanges
     */
    readonly type?: GetUserPointChangesTypeEnum

    /**
     * 
     * @type {string}
     * @memberof UserPointApiGetUserPointChanges
     */
    readonly user?: string

    /**
     * 
     * @type {number}
     * @memberof UserPointApiGetUserPointChanges
     */
    readonly offset?: number

    /**
     * 
     * @type {number}
     * @memberof UserPointApiGetUserPointChanges
     */
    readonly limit?: number
}

/**
 * Request parameters for getUserPointValue operation in UserPointApi.
 * @export
 * @interface UserPointApiGetUserPointValueRequest
 */
export interface UserPointApiGetUserPointValueRequest {
    /**
     * 
     * @type {string}
     * @memberof UserPointApiGetUserPointValue
     */
    readonly key: string
}

/**
 * UserPointApi - object-oriented interface
 * @export
 * @class UserPointApi
 * @extends {BaseAPI}
 */
export class UserPointApi extends BaseAPI {
    /**
     * 
     * @summary 获取当前用户的数值变化记录总和。（管理员能传入参数 user 获取指定用户的数值变化记录。）一次最多查询 50 条。
     * @param {UserPointApiCountRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof UserPointApi
     */
    public count(requestParameters: UserPointApiCountRequest, options?: RawAxiosRequestConfig) {
        return UserPointApiFp(this.configuration).count(requestParameters.key, requestParameters.type, requestParameters.user, requestParameters.start, requestParameters.end, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 获取当前用户的数值变化记录。（管理员能传入参数 user 获取指定用户的数值变化记录。）一次最多查询 50 条。
     * @param {UserPointApiGetUserPointChangesRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof UserPointApi
     */
    public getUserPointChanges(requestParameters: UserPointApiGetUserPointChangesRequest, options?: RawAxiosRequestConfig) {
        return UserPointApiFp(this.configuration).getUserPointChanges(requestParameters.key, requestParameters.type, requestParameters.user, requestParameters.offset, requestParameters.limit, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 获取所有用户数值的 key 列表。
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof UserPointApi
     */
    public getUserPointKeys1(options?: RawAxiosRequestConfig) {
        return UserPointApiFp(this.configuration).getUserPointKeys1(options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 获取当前用户指定 key 的用户数值。
     * @param {UserPointApiGetUserPointValueRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof UserPointApi
     */
    public getUserPointValue(requestParameters: UserPointApiGetUserPointValueRequest, options?: RawAxiosRequestConfig) {
        return UserPointApiFp(this.configuration).getUserPointValue(requestParameters.key, options).then((request) => request(this.axios, this.basePath));
    }
}

/**
 * @export
 */
export const CountTypeEnum = {
    Increase: 'INCREASE',
    Decrease: 'DECREASE'
} as const;
export type CountTypeEnum = typeof CountTypeEnum[keyof typeof CountTypeEnum];
/**
 * @export
 */
export const GetUserPointChangesTypeEnum = {
    Increase: 'INCREASE',
    Decrease: 'DECREASE'
} as const;
export type GetUserPointChangesTypeEnum = typeof GetUserPointChangesTypeEnum[keyof typeof GetUserPointChangesTypeEnum];


/**
 * UserQAApi - axios parameter creator
 * @export
 */
export const UserQAApiAxiosParamCreator = function (configuration?: Configuration) {
    return {
        /**
         * 
         * @summary 解绑用户角色。
         * @param {string} id 用户id或者角色id
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        unbindRole: async (id: string, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'id' is not null or undefined
            assertParamExists('unbindRole', 'id', id)
            const localVarPath = `/api/v1/qa/user/role-unbind`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'POST', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)

            if (id !== undefined) {
                localVarQueryParameter['id'] = id;
            }



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
    }
};

/**
 * UserQAApi - functional programming interface
 * @export
 */
export const UserQAApiFp = function (configuration?: Configuration) {
    const localVarAxiosParamCreator = UserQAApiAxiosParamCreator(configuration)
    return {
        /**
         * 
         * @summary 解绑用户角色。
         * @param {string} id 用户id或者角色id
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async unbindRole(id: string, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<void>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.unbindRole(id, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['UserQAApi.unbindRole']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
    }
};

/**
 * UserQAApi - factory interface
 * @export
 */
export const UserQAApiFactory = function (configuration?: Configuration, basePath?: string, axios?: AxiosInstance) {
    const localVarFp = UserQAApiFp(configuration)
    return {
        /**
         * 
         * @summary 解绑用户角色。
         * @param {UserQAApiUnbindRoleRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        unbindRole(requestParameters: UserQAApiUnbindRoleRequest, options?: RawAxiosRequestConfig): AxiosPromise<void> {
            return localVarFp.unbindRole(requestParameters.id, options).then((request) => request(axios, basePath));
        },
    };
};

/**
 * Request parameters for unbindRole operation in UserQAApi.
 * @export
 * @interface UserQAApiUnbindRoleRequest
 */
export interface UserQAApiUnbindRoleRequest {
    /**
     * 用户id或者角色id
     * @type {string}
     * @memberof UserQAApiUnbindRole
     */
    readonly id: string
}

/**
 * UserQAApi - object-oriented interface
 * @export
 * @class UserQAApi
 * @extends {BaseAPI}
 */
export class UserQAApi extends BaseAPI {
    /**
     * 
     * @summary 解绑用户角色。
     * @param {UserQAApiUnbindRoleRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof UserQAApi
     */
    public unbindRole(requestParameters: UserQAApiUnbindRoleRequest, options?: RawAxiosRequestConfig) {
        return UserQAApiFp(this.configuration).unbindRole(requestParameters.id, options).then((request) => request(this.axios, this.basePath));
    }
}



/**
 * UsersApi - axios parameter creator
 * @export
 */
export const UsersApiAxiosParamCreator = function (configuration?: Configuration) {
    return {
        /**
         * 
         * @summary 获取当前管理员。
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getAdminUser: async (options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            const localVarPath = `/api/v1/admin-user`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 获取当前用户。
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getCurrentUser: async (options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            const localVarPath = `/api/v1/user`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
    }
};

/**
 * UsersApi - functional programming interface
 * @export
 */
export const UsersApiFp = function (configuration?: Configuration) {
    const localVarAxiosParamCreator = UsersApiAxiosParamCreator(configuration)
    return {
        /**
         * 
         * @summary 获取当前管理员。
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async getAdminUser(options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<User>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.getAdminUser(options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['UsersApi.getAdminUser']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 获取当前用户。
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async getCurrentUser(options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<User>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.getCurrentUser(options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['UsersApi.getCurrentUser']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
    }
};

/**
 * UsersApi - factory interface
 * @export
 */
export const UsersApiFactory = function (configuration?: Configuration, basePath?: string, axios?: AxiosInstance) {
    const localVarFp = UsersApiFp(configuration)
    return {
        /**
         * 
         * @summary 获取当前管理员。
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getAdminUser(options?: RawAxiosRequestConfig): AxiosPromise<User> {
            return localVarFp.getAdminUser(options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 获取当前用户。
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getCurrentUser(options?: RawAxiosRequestConfig): AxiosPromise<User> {
            return localVarFp.getCurrentUser(options).then((request) => request(axios, basePath));
        },
    };
};

/**
 * UsersApi - object-oriented interface
 * @export
 * @class UsersApi
 * @extends {BaseAPI}
 */
export class UsersApi extends BaseAPI {
    /**
     * 
     * @summary 获取当前管理员。
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof UsersApi
     */
    public getAdminUser(options?: RawAxiosRequestConfig) {
        return UsersApiFp(this.configuration).getAdminUser(options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 获取当前用户。
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof UsersApi
     */
    public getCurrentUser(options?: RawAxiosRequestConfig) {
        return UsersApiFp(this.configuration).getCurrentUser(options).then((request) => request(this.axios, this.basePath));
    }
}



/**
 * WechatCommonApi - axios parameter creator
 * @export
 */
export const WechatCommonApiAxiosParamCreator = function (configuration?: Configuration) {
    return {
        /**
         * 
         * @summary 通过 unionId 获取用户。
         * @param {Set<string>} unionId 
         * @param {string} xAppId 应用ID
         * @param {string} xAppSignature 应用签名
         * @param {string} xAppDate 应用时间戳
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        findWechatUsers: async (unionId: Set<string>, xAppId: string, xAppSignature: string, xAppDate: string, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'unionId' is not null or undefined
            assertParamExists('findWechatUsers', 'unionId', unionId)
            // verify required parameter 'xAppId' is not null or undefined
            assertParamExists('findWechatUsers', 'xAppId', xAppId)
            // verify required parameter 'xAppSignature' is not null or undefined
            assertParamExists('findWechatUsers', 'xAppSignature', xAppSignature)
            // verify required parameter 'xAppDate' is not null or undefined
            assertParamExists('findWechatUsers', 'xAppDate', xAppDate)
            const localVarPath = `/api/v1/wechat/common/users`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            if (unionId) {
                localVarQueryParameter['unionId'] = Array.from(unionId);
            }



            if (xAppId != null) {
                localVarHeaderParameter['X-App-Id'] = String(xAppId);
            }
            if (xAppSignature != null) {
                localVarHeaderParameter['X-App-Signature'] = String(xAppSignature);
            }
            if (xAppDate != null) {
                localVarHeaderParameter['X-App-Date'] = String(xAppDate);
            }
            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
    }
};

/**
 * WechatCommonApi - functional programming interface
 * @export
 */
export const WechatCommonApiFp = function (configuration?: Configuration) {
    const localVarAxiosParamCreator = WechatCommonApiAxiosParamCreator(configuration)
    return {
        /**
         * 
         * @summary 通过 unionId 获取用户。
         * @param {Set<string>} unionId 
         * @param {string} xAppId 应用ID
         * @param {string} xAppSignature 应用签名
         * @param {string} xAppDate 应用时间戳
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async findWechatUsers(unionId: Set<string>, xAppId: string, xAppSignature: string, xAppDate: string, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<Array<User>>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.findWechatUsers(unionId, xAppId, xAppSignature, xAppDate, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['WechatCommonApi.findWechatUsers']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
    }
};

/**
 * WechatCommonApi - factory interface
 * @export
 */
export const WechatCommonApiFactory = function (configuration?: Configuration, basePath?: string, axios?: AxiosInstance) {
    const localVarFp = WechatCommonApiFp(configuration)
    return {
        /**
         * 
         * @summary 通过 unionId 获取用户。
         * @param {WechatCommonApiFindWechatUsersRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        findWechatUsers(requestParameters: WechatCommonApiFindWechatUsersRequest, options?: RawAxiosRequestConfig): AxiosPromise<Array<User>> {
            return localVarFp.findWechatUsers(requestParameters.unionId, requestParameters.xAppId, requestParameters.xAppSignature, requestParameters.xAppDate, options).then((request) => request(axios, basePath));
        },
    };
};

/**
 * Request parameters for findWechatUsers operation in WechatCommonApi.
 * @export
 * @interface WechatCommonApiFindWechatUsersRequest
 */
export interface WechatCommonApiFindWechatUsersRequest {
    /**
     * 
     * @type {Set<string>}
     * @memberof WechatCommonApiFindWechatUsers
     */
    readonly unionId: Set<string>

    /**
     * 应用ID
     * @type {string}
     * @memberof WechatCommonApiFindWechatUsers
     */
    readonly xAppId: string

    /**
     * 应用签名
     * @type {string}
     * @memberof WechatCommonApiFindWechatUsers
     */
    readonly xAppSignature: string

    /**
     * 应用时间戳
     * @type {string}
     * @memberof WechatCommonApiFindWechatUsers
     */
    readonly xAppDate: string
}

/**
 * WechatCommonApi - object-oriented interface
 * @export
 * @class WechatCommonApi
 * @extends {BaseAPI}
 */
export class WechatCommonApi extends BaseAPI {
    /**
     * 
     * @summary 通过 unionId 获取用户。
     * @param {WechatCommonApiFindWechatUsersRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof WechatCommonApi
     */
    public findWechatUsers(requestParameters: WechatCommonApiFindWechatUsersRequest, options?: RawAxiosRequestConfig) {
        return WechatCommonApiFp(this.configuration).findWechatUsers(requestParameters.unionId, requestParameters.xAppId, requestParameters.xAppSignature, requestParameters.xAppDate, options).then((request) => request(this.axios, this.basePath));
    }
}



/**
 * WechatMiniProgramApi - axios parameter creator
 * @export
 */
export const WechatMiniProgramApiAxiosParamCreator = function (configuration?: Configuration) {
    return {
        /**
         * 
         * @summary 通过微信绑定手机号。
         * @param {string} code 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        bindPhoneByWechat1: async (code: string, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'code' is not null or undefined
            assertParamExists('bindPhoneByWechat1', 'code', code)
            const localVarPath = `/api/v1/wechat/mp/phone-binding`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'POST', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)

            if (code !== undefined) {
                localVarQueryParameter['code'] = code;
            }



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 通过微信小程序的 code 获取 token。
         * @param {string} code 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        generateToken: async (code: string, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'code' is not null or undefined
            assertParamExists('generateToken', 'code', code)
            const localVarPath = `/api/v1/wechat/mp/token`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'POST', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            if (code !== undefined) {
                localVarQueryParameter['code'] = code;
            }



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 获取小程序链接。
         * @param {string} [key] 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getMiniProgramLink: async (key?: string, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            const localVarPath = `/api/v1/wechat/mp/link`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'POST', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            if (key !== undefined) {
                localVarQueryParameter['key'] = key;
            }



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 跳转到小程序链接。
         * @param {string} [key] 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        redirectMiniProgramLink: async (key?: string, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            const localVarPath = `/api/v1/wechat/mp/link`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'GET', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            if (key !== undefined) {
                localVarQueryParameter['key'] = key;
            }



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
    }
};

/**
 * WechatMiniProgramApi - functional programming interface
 * @export
 */
export const WechatMiniProgramApiFp = function (configuration?: Configuration) {
    const localVarAxiosParamCreator = WechatMiniProgramApiAxiosParamCreator(configuration)
    return {
        /**
         * 
         * @summary 通过微信绑定手机号。
         * @param {string} code 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async bindPhoneByWechat1(code: string, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<User>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.bindPhoneByWechat1(code, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['WechatMiniProgramApi.bindPhoneByWechat1']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 通过微信小程序的 code 获取 token。
         * @param {string} code 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async generateToken(code: string, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<string>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.generateToken(code, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['WechatMiniProgramApi.generateToken']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 获取小程序链接。
         * @param {string} [key] 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async getMiniProgramLink(key?: string, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<string>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.getMiniProgramLink(key, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['WechatMiniProgramApi.getMiniProgramLink']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 跳转到小程序链接。
         * @param {string} [key] 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async redirectMiniProgramLink(key?: string, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<ErrorDetails>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.redirectMiniProgramLink(key, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['WechatMiniProgramApi.redirectMiniProgramLink']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
    }
};

/**
 * WechatMiniProgramApi - factory interface
 * @export
 */
export const WechatMiniProgramApiFactory = function (configuration?: Configuration, basePath?: string, axios?: AxiosInstance) {
    const localVarFp = WechatMiniProgramApiFp(configuration)
    return {
        /**
         * 
         * @summary 通过微信绑定手机号。
         * @param {WechatMiniProgramApiBindPhoneByWechat1Request} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        bindPhoneByWechat1(requestParameters: WechatMiniProgramApiBindPhoneByWechat1Request, options?: RawAxiosRequestConfig): AxiosPromise<User> {
            return localVarFp.bindPhoneByWechat1(requestParameters.code, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 通过微信小程序的 code 获取 token。
         * @param {WechatMiniProgramApiGenerateTokenRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        generateToken(requestParameters: WechatMiniProgramApiGenerateTokenRequest, options?: RawAxiosRequestConfig): AxiosPromise<string> {
            return localVarFp.generateToken(requestParameters.code, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 获取小程序链接。
         * @param {WechatMiniProgramApiGetMiniProgramLinkRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getMiniProgramLink(requestParameters: WechatMiniProgramApiGetMiniProgramLinkRequest = {}, options?: RawAxiosRequestConfig): AxiosPromise<string> {
            return localVarFp.getMiniProgramLink(requestParameters.key, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 跳转到小程序链接。
         * @param {WechatMiniProgramApiRedirectMiniProgramLinkRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        redirectMiniProgramLink(requestParameters: WechatMiniProgramApiRedirectMiniProgramLinkRequest = {}, options?: RawAxiosRequestConfig): AxiosPromise<ErrorDetails> {
            return localVarFp.redirectMiniProgramLink(requestParameters.key, options).then((request) => request(axios, basePath));
        },
    };
};

/**
 * Request parameters for bindPhoneByWechat1 operation in WechatMiniProgramApi.
 * @export
 * @interface WechatMiniProgramApiBindPhoneByWechat1Request
 */
export interface WechatMiniProgramApiBindPhoneByWechat1Request {
    /**
     * 
     * @type {string}
     * @memberof WechatMiniProgramApiBindPhoneByWechat1
     */
    readonly code: string
}

/**
 * Request parameters for generateToken operation in WechatMiniProgramApi.
 * @export
 * @interface WechatMiniProgramApiGenerateTokenRequest
 */
export interface WechatMiniProgramApiGenerateTokenRequest {
    /**
     * 
     * @type {string}
     * @memberof WechatMiniProgramApiGenerateToken
     */
    readonly code: string
}

/**
 * Request parameters for getMiniProgramLink operation in WechatMiniProgramApi.
 * @export
 * @interface WechatMiniProgramApiGetMiniProgramLinkRequest
 */
export interface WechatMiniProgramApiGetMiniProgramLinkRequest {
    /**
     * 
     * @type {string}
     * @memberof WechatMiniProgramApiGetMiniProgramLink
     */
    readonly key?: string
}

/**
 * Request parameters for redirectMiniProgramLink operation in WechatMiniProgramApi.
 * @export
 * @interface WechatMiniProgramApiRedirectMiniProgramLinkRequest
 */
export interface WechatMiniProgramApiRedirectMiniProgramLinkRequest {
    /**
     * 
     * @type {string}
     * @memberof WechatMiniProgramApiRedirectMiniProgramLink
     */
    readonly key?: string
}

/**
 * WechatMiniProgramApi - object-oriented interface
 * @export
 * @class WechatMiniProgramApi
 * @extends {BaseAPI}
 */
export class WechatMiniProgramApi extends BaseAPI {
    /**
     * 
     * @summary 通过微信绑定手机号。
     * @param {WechatMiniProgramApiBindPhoneByWechat1Request} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof WechatMiniProgramApi
     */
    public bindPhoneByWechat1(requestParameters: WechatMiniProgramApiBindPhoneByWechat1Request, options?: RawAxiosRequestConfig) {
        return WechatMiniProgramApiFp(this.configuration).bindPhoneByWechat1(requestParameters.code, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 通过微信小程序的 code 获取 token。
     * @param {WechatMiniProgramApiGenerateTokenRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof WechatMiniProgramApi
     */
    public generateToken(requestParameters: WechatMiniProgramApiGenerateTokenRequest, options?: RawAxiosRequestConfig) {
        return WechatMiniProgramApiFp(this.configuration).generateToken(requestParameters.code, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 获取小程序链接。
     * @param {WechatMiniProgramApiGetMiniProgramLinkRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof WechatMiniProgramApi
     */
    public getMiniProgramLink(requestParameters: WechatMiniProgramApiGetMiniProgramLinkRequest = {}, options?: RawAxiosRequestConfig) {
        return WechatMiniProgramApiFp(this.configuration).getMiniProgramLink(requestParameters.key, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 跳转到小程序链接。
     * @param {WechatMiniProgramApiRedirectMiniProgramLinkRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof WechatMiniProgramApi
     */
    public redirectMiniProgramLink(requestParameters: WechatMiniProgramApiRedirectMiniProgramLinkRequest = {}, options?: RawAxiosRequestConfig) {
        return WechatMiniProgramApiFp(this.configuration).redirectMiniProgramLink(requestParameters.key, options).then((request) => request(this.axios, this.basePath));
    }
}



/**
 * WechatMiniProgramQaApi - axios parameter creator
 * @export
 */
export const WechatMiniProgramQaApiAxiosParamCreator = function (configuration?: Configuration) {
    return {
        /**
         * 
         * @summary 通过微信绑定手机号。
         * @param {string} openid 
         * @param {string} phone 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        bindPhoneByWechat: async (openid: string, phone: string, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'openid' is not null or undefined
            assertParamExists('bindPhoneByWechat', 'openid', openid)
            // verify required parameter 'phone' is not null or undefined
            assertParamExists('bindPhoneByWechat', 'phone', phone)
            const localVarPath = `/api/v1/wechat/mp/qa/phone-binding`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'POST', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)

            if (openid !== undefined) {
                localVarQueryParameter['openid'] = openid;
            }

            if (phone !== undefined) {
                localVarQueryParameter['phone'] = phone;
            }



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary 管理员创建用户并生成 Token。
         * @param {string} openId 
         * @param {string} [unionId] 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        generateToken1: async (openId: string, unionId?: string, options: RawAxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'openId' is not null or undefined
            assertParamExists('generateToken1', 'openId', openId)
            const localVarPath = `/api/v1/wechat/mp/qa/token`;
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions = { method: 'POST', ...baseOptions, ...options };
            const localVarHeaderParameter = {} as any;
            const localVarQueryParameter = {} as any;

            // authentication AccessToken required
            // http bearer authentication required
            await setBearerAuthToObject(localVarHeaderParameter, configuration)

            if (openId !== undefined) {
                localVarQueryParameter['openId'] = openId;
            }

            if (unionId !== undefined) {
                localVarQueryParameter['unionId'] = unionId;
            }



            setSearchParams(localVarUrlObj, localVarQueryParameter);
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = { ...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers };

            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
    }
};

/**
 * WechatMiniProgramQaApi - functional programming interface
 * @export
 */
export const WechatMiniProgramQaApiFp = function (configuration?: Configuration) {
    const localVarAxiosParamCreator = WechatMiniProgramQaApiAxiosParamCreator(configuration)
    return {
        /**
         * 
         * @summary 通过微信绑定手机号。
         * @param {string} openid 
         * @param {string} phone 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async bindPhoneByWechat(openid: string, phone: string, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<User>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.bindPhoneByWechat(openid, phone, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['WechatMiniProgramQaApi.bindPhoneByWechat']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
        /**
         * 
         * @summary 管理员创建用户并生成 Token。
         * @param {string} openId 
         * @param {string} [unionId] 
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async generateToken1(openId: string, unionId?: string, options?: RawAxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<string>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.generateToken1(openId, unionId, options);
            const localVarOperationServerIndex = configuration?.serverIndex ?? 0;
            const localVarOperationServerBasePath = operationServerMap['WechatMiniProgramQaApi.generateToken1']?.[localVarOperationServerIndex]?.url;
            return (axios, basePath) => createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration)(axios, localVarOperationServerBasePath || basePath);
        },
    }
};

/**
 * WechatMiniProgramQaApi - factory interface
 * @export
 */
export const WechatMiniProgramQaApiFactory = function (configuration?: Configuration, basePath?: string, axios?: AxiosInstance) {
    const localVarFp = WechatMiniProgramQaApiFp(configuration)
    return {
        /**
         * 
         * @summary 通过微信绑定手机号。
         * @param {WechatMiniProgramQaApiBindPhoneByWechatRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        bindPhoneByWechat(requestParameters: WechatMiniProgramQaApiBindPhoneByWechatRequest, options?: RawAxiosRequestConfig): AxiosPromise<User> {
            return localVarFp.bindPhoneByWechat(requestParameters.openid, requestParameters.phone, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary 管理员创建用户并生成 Token。
         * @param {WechatMiniProgramQaApiGenerateToken1Request} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        generateToken1(requestParameters: WechatMiniProgramQaApiGenerateToken1Request, options?: RawAxiosRequestConfig): AxiosPromise<string> {
            return localVarFp.generateToken1(requestParameters.openId, requestParameters.unionId, options).then((request) => request(axios, basePath));
        },
    };
};

/**
 * Request parameters for bindPhoneByWechat operation in WechatMiniProgramQaApi.
 * @export
 * @interface WechatMiniProgramQaApiBindPhoneByWechatRequest
 */
export interface WechatMiniProgramQaApiBindPhoneByWechatRequest {
    /**
     * 
     * @type {string}
     * @memberof WechatMiniProgramQaApiBindPhoneByWechat
     */
    readonly openid: string

    /**
     * 
     * @type {string}
     * @memberof WechatMiniProgramQaApiBindPhoneByWechat
     */
    readonly phone: string
}

/**
 * Request parameters for generateToken1 operation in WechatMiniProgramQaApi.
 * @export
 * @interface WechatMiniProgramQaApiGenerateToken1Request
 */
export interface WechatMiniProgramQaApiGenerateToken1Request {
    /**
     * 
     * @type {string}
     * @memberof WechatMiniProgramQaApiGenerateToken1
     */
    readonly openId: string

    /**
     * 
     * @type {string}
     * @memberof WechatMiniProgramQaApiGenerateToken1
     */
    readonly unionId?: string
}

/**
 * WechatMiniProgramQaApi - object-oriented interface
 * @export
 * @class WechatMiniProgramQaApi
 * @extends {BaseAPI}
 */
export class WechatMiniProgramQaApi extends BaseAPI {
    /**
     * 
     * @summary 通过微信绑定手机号。
     * @param {WechatMiniProgramQaApiBindPhoneByWechatRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof WechatMiniProgramQaApi
     */
    public bindPhoneByWechat(requestParameters: WechatMiniProgramQaApiBindPhoneByWechatRequest, options?: RawAxiosRequestConfig) {
        return WechatMiniProgramQaApiFp(this.configuration).bindPhoneByWechat(requestParameters.openid, requestParameters.phone, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary 管理员创建用户并生成 Token。
     * @param {WechatMiniProgramQaApiGenerateToken1Request} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof WechatMiniProgramQaApi
     */
    public generateToken1(requestParameters: WechatMiniProgramQaApiGenerateToken1Request, options?: RawAxiosRequestConfig) {
        return WechatMiniProgramQaApiFp(this.configuration).generateToken1(requestParameters.openId, requestParameters.unionId, options).then((request) => request(this.axios, this.basePath));
    }
}




```

### node_modules\@everdev\lsdmxmp-client\base.ts
```typescript
/* tslint:disable */
/* eslint-disable */
/**
 * lsdmx-mp Server API Document
 * lsdmx-mp 服务端接口文档
 *
 * The version of the OpenAPI document: v0.0.1-SNAPSHOT
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


import type { Configuration } from '@everdev/lsdmxmp-client/configuration';
// Some imports not used depending on template conditions
// @ts-ignore
import type { AxiosPromise, AxiosInstance, RawAxiosRequestConfig } from 'axios';
import globalAxios from 'axios';

export const BASE_PATH = "http://localhost:8080".replace(/\/+$/, "");

/**
 *
 * @export
 */
export const COLLECTION_FORMATS = {
    csv: ",",
    ssv: " ",
    tsv: "\t",
    pipes: "|",
};

/**
 *
 * @export
 * @interface RequestArgs
 */
export interface RequestArgs {
    url: string;
    options: RawAxiosRequestConfig;
}

/**
 *
 * @export
 * @class BaseAPI
 */
export class BaseAPI {
    protected configuration: Configuration | undefined;

    constructor(configuration?: Configuration, protected basePath: string = BASE_PATH, protected axios: AxiosInstance = globalAxios) {
        if (configuration) {
            this.configuration = configuration;
            this.basePath = configuration.basePath ?? basePath;
        }
    }
};

/**
 *
 * @export
 * @class RequiredError
 * @extends {Error}
 */
export class RequiredError extends Error {
    constructor(public field: string, msg?: string) {
        super(msg);
        this.name = "RequiredError"
    }
}

interface ServerMap {
    [key: string]: {
        url: string,
        description: string,
    }[];
}

/**
 *
 * @export
 */
export const operationServerMap: ServerMap = {
}

```

### node_modules\@everdev\lsdmxmp-client\common.ts
```typescript
/* tslint:disable */
/* eslint-disable */
/**
 * lsdmx-mp Server API Document
 * lsdmx-mp 服务端接口文档
 *
 * The version of the OpenAPI document: v0.0.1-SNAPSHOT
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


import type { Configuration } from "@everdev/lsdmxmp-client/configuration";
import type { RequestArgs } from "@everdev/lsdmxmp-client/base";
import type { AxiosInstance, AxiosResponse } from 'axios';
import { RequiredError } from "@everdev/lsdmxmp-client/base";

/**
 *
 * @export
 */
export const DUMMY_BASE_URL = 'https://example.com'

/**
 *
 * @throws {RequiredError}
 * @export
 */
export const assertParamExists = function (functionName: string, paramName: string, paramValue: unknown) {
    if (paramValue === null || paramValue === undefined) {
        throw new RequiredError(paramName, `Required parameter ${paramName} was null or undefined when calling ${functionName}.`);
    }
}

/**
 *
 * @export
 */
export const setApiKeyToObject = async function (object: any, keyParamName: string, configuration?: Configuration) {
    if (configuration && configuration.apiKey) {
        const localVarApiKeyValue = typeof configuration.apiKey === 'function'
            ? await configuration.apiKey(keyParamName)
            : await configuration.apiKey;
        object[keyParamName] = localVarApiKeyValue;
    }
}

/**
 *
 * @export
 */
export const setBasicAuthToObject = function (object: any, configuration?: Configuration) {
    if (configuration && (configuration.username || configuration.password)) {
        object["auth"] = { username: configuration.username, password: configuration.password };
    }
}

/**
 *
 * @export
 */
export const setBearerAuthToObject = async function (object: any, configuration?: Configuration) {
    if (configuration && configuration.accessToken) {
        const accessToken = typeof configuration.accessToken === 'function'
            ? await configuration.accessToken()
            : await configuration.accessToken;
        object["Authorization"] = "Bearer " + accessToken;
    }
}

/**
 *
 * @export
 */
export const setOAuthToObject = async function (object: any, name: string, scopes: string[], configuration?: Configuration) {
    if (configuration && configuration.accessToken) {
        const localVarAccessTokenValue = typeof configuration.accessToken === 'function'
            ? await configuration.accessToken(name, scopes)
            : await configuration.accessToken;
        object["Authorization"] = "Bearer " + localVarAccessTokenValue;
    }
}

function setFlattenedQueryParams(urlSearchParams: URLSearchParams, parameter: any, key: string = ""): void {
    if (parameter == null) return;
    if (typeof parameter === "object") {
        if (Array.isArray(parameter)) {
            (parameter as any[]).forEach(item => setFlattenedQueryParams(urlSearchParams, item, key));
        }
        else {
            Object.keys(parameter).forEach(currentKey =>
                setFlattenedQueryParams(urlSearchParams, parameter[currentKey], `${key}${key !== '' ? '.' : ''}${currentKey}`)
            );
        }
    }
    else {
        if (urlSearchParams.has(key)) {
            urlSearchParams.append(key, parameter);
        }
        else {
            urlSearchParams.set(key, parameter);
        }
    }
}

/**
 *
 * @export
 */
export const setSearchParams = function (url: URL, ...objects: any[]) {
    const searchParams = new URLSearchParams(url.search);
    setFlattenedQueryParams(searchParams, objects);
    url.search = searchParams.toString();
}

/**
 *
 * @export
 */
export const serializeDataIfNeeded = function (value: any, requestOptions: any, configuration?: Configuration) {
    const nonString = typeof value !== 'string';
    const needsSerialization = nonString && configuration && configuration.isJsonMime
        ? configuration.isJsonMime(requestOptions.headers['Content-Type'])
        : nonString;
    return needsSerialization
        ? JSON.stringify(value !== undefined ? value : {})
        : (value || "");
}

/**
 *
 * @export
 */
export const toPathString = function (url: URL) {
    return url.pathname + url.search + url.hash
}

/**
 *
 * @export
 */
export const createRequestFunction = function (axiosArgs: RequestArgs, globalAxios: AxiosInstance, BASE_PATH: string, configuration?: Configuration) {
    return <T = unknown, R = AxiosResponse<T>>(axios: AxiosInstance = globalAxios, basePath: string = BASE_PATH) => {
        const axiosRequestArgs = { ...axiosArgs.options, url: (axios.defaults.baseURL ? '' : configuration?.basePath ?? basePath) + axiosArgs.url };
        return axios.request<T, R>(axiosRequestArgs);
    };
}

```

### node_modules\@everdev\lsdmxmp-client\configuration.ts
```typescript
/* tslint:disable */
/* eslint-disable */
/**
 * lsdmx-mp Server API Document
 * lsdmx-mp 服务端接口文档
 *
 * The version of the OpenAPI document: v0.0.1-SNAPSHOT
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


export interface ConfigurationParameters {
    apiKey?: string | Promise<string> | ((name: string) => string) | ((name: string) => Promise<string>);
    username?: string;
    password?: string;
    accessToken?: string | Promise<string> | ((name?: string, scopes?: string[]) => string) | ((name?: string, scopes?: string[]) => Promise<string>);
    basePath?: string;
    serverIndex?: number;
    baseOptions?: any;
    formDataCtor?: new () => any;
}

export class Configuration {
    /**
     * parameter for apiKey security
     * @param name security name
     * @memberof Configuration
     */
    apiKey?: string | Promise<string> | ((name: string) => string) | ((name: string) => Promise<string>);
    /**
     * parameter for basic security
     *
     * @type {string}
     * @memberof Configuration
     */
    username?: string;
    /**
     * parameter for basic security
     *
     * @type {string}
     * @memberof Configuration
     */
    password?: string;
    /**
     * parameter for oauth2 security
     * @param name security name
     * @param scopes oauth2 scope
     * @memberof Configuration
     */
    accessToken?: string | Promise<string> | ((name?: string, scopes?: string[]) => string) | ((name?: string, scopes?: string[]) => Promise<string>);
    /**
     * override base path
     *
     * @type {string}
     * @memberof Configuration
     */
    basePath?: string;
    /**
     * override server index
     *
     * @type {number}
     * @memberof Configuration
     */
    serverIndex?: number;
    /**
     * base options for axios calls
     *
     * @type {any}
     * @memberof Configuration
     */
    baseOptions?: any;
    /**
     * The FormData constructor that will be used to create multipart form data
     * requests. You can inject this here so that execution environments that
     * do not support the FormData class can still run the generated client.
     *
     * @type {new () => FormData}
     */
    formDataCtor?: new () => any;

    constructor(param: ConfigurationParameters = {}) {
        this.apiKey = param.apiKey;
        this.username = param.username;
        this.password = param.password;
        this.accessToken = param.accessToken;
        this.basePath = param.basePath;
        this.serverIndex = param.serverIndex;
        this.baseOptions = {
            ...param.baseOptions,
            headers: {
                ...param.baseOptions?.headers,
            },
        };
        this.formDataCtor = param.formDataCtor;
    }

    /**
     * Check if the given MIME is a JSON MIME.
     * JSON MIME examples:
     *   application/json
     *   application/json; charset=UTF8
     *   APPLICATION/JSON
     *   application/vnd.company+json
     * @param mime - MIME (Multipurpose Internet Mail Extensions)
     * @return True if the given MIME is JSON, false otherwise.
     */
    public isJsonMime(mime: string): boolean {
        const jsonMime: RegExp = new RegExp('^(application\/json|[^;/ \t]+\/[^;/ \t]+[+]json)[ \t]*(;.*)?$', 'i');
        return mime !== null && (jsonMime.test(mime) || mime.toLowerCase() === 'application/json-patch+json');
    }
}

```

### node_modules\@everdev\lsdmxmp-client\git_push.sh
```bash
#!/bin/sh
# ref: https://help.github.com/articles/adding-an-existing-project-to-github-using-the-command-line/
#
# Usage example: /bin/sh ./git_push.sh wing328 openapi-petstore-perl "minor update" "gitlab.com"

git_user_id=$1
git_repo_id=$2
release_note=$3
git_host=$4

if [ "$git_host" = "" ]; then
    git_host="github.com"
    echo "[INFO] No command line input provided. Set \$git_host to $git_host"
fi

if [ "$git_user_id" = "" ]; then
    git_user_id="GIT_USER_ID"
    echo "[INFO] No command line input provided. Set \$git_user_id to $git_user_id"
fi

if [ "$git_repo_id" = "" ]; then
    git_repo_id="GIT_REPO_ID"
    echo "[INFO] No command line input provided. Set \$git_repo_id to $git_repo_id"
fi

if [ "$release_note" = "" ]; then
    release_note="Minor update"
    echo "[INFO] No command line input provided. Set \$release_note to $release_note"
fi

# Initialize the local directory as a Git repository
git init

# Adds the files in the local repository and stages them for commit.
git add .

# Commits the tracked changes and prepares them to be pushed to a remote repository.
git commit -m "$release_note"

# Sets the new remote
git_remote=$(git remote)
if [ "$git_remote" = "" ]; then # git remote not defined

    if [ "$GIT_TOKEN" = "" ]; then
        echo "[INFO] \$GIT_TOKEN (environment variable) is not set. Using the git credential in your environment."
        git remote add origin https://${git_host}/${git_user_id}/${git_repo_id}.git
    else
        git remote add origin https://${git_user_id}:"${GIT_TOKEN}"@${git_host}/${git_user_id}/${git_repo_id}.git
    fi

fi

git pull origin master

# Pushes (Forces) the changes in the local repository up to the remote repository
echo "Git pushing to https://${git_host}/${git_user_id}/${git_repo_id}.git"
git push origin master 2>&1 | grep -v 'To https'

```

### node_modules\@everdev\lsdmxmp-client\index.ts
```typescript
/* tslint:disable */
/* eslint-disable */
/**
 * lsdmx-mp Server API Document
 * lsdmx-mp 服务端接口文档
 *
 * The version of the OpenAPI document: v0.0.1-SNAPSHOT
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


export * from "@everdev/lsdmxmp-client/api";
export * from "@everdev/lsdmxmp-client/configuration";


```

### node_modules\@everdev\lsdmxmp-client\package.json
```json
{
  "name": "@everdev/lsdmxmp-client",
  "version": "0.0.1-SNAPSHOT-dev",
  "description": "",
  "main": "index.ts",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "dependencies": {
    "axios": "^0.21.1"
  },
   "publishConfig": {
     "registry": "http://repo-everdev.nie.netease.com/repository/npm-hosted/"
   }
}

```

### node_modules\@everdev\lsdmxmp-client\tsconfig.json
```json
{
  "compilerOptions": {
    "module": "commonjs",
    "target": "es6",
    "noImplicitAny": false,
    "sourceMap": false,
    "rootDir": "./",
    "outDir": "../javascript",
    "esModuleInterop": true,
    "declaration": true
  },
  "include": [
    "./**/*",
    "./*"
  ],
  "exclude": []
}

```

### node_modules\axios\CHANGELOG.md
```markdown
# Changelog

### 0.21.4 (September 6, 2021)

Fixes and Functionality:
- Fixing JSON transform when data is stringified. Providing backward compatibility and complying to the JSON RFC standard ([#4020](https://github.com/axios/axios/pull/4020))

Huge thanks to everyone who contributed to this release via code (authors listed below) or via reviews and triaging on GitHub:

- [Jay](mailto:jasonsaayman@gmail.com)
- [Guillaume Fortaine](https://github.com/gfortaine)
- [Yusuke Kawasaki](https://github.com/kawanet)
- [Dmitriy Mozgovoy](https://github.com/DigitalBrainJS)

### 0.21.3 (September 4, 2021)

Fixes and Functionality:
- Fixing response interceptor not being called when request interceptor is attached ([#4013](https://github.com/axios/axios/pull/4013))

Huge thanks to everyone who contributed to this release via code (authors listed below) or via reviews and triaging on GitHub:

- [Jay](mailto:jasonsaayman@gmail.com)
- [Julian Hollmann](https://github.com/nerdbeere)

### 0.21.2 (September 4, 2021)

Fixes and Functionality:

- Updating axios requests to be delayed by pre-emptive promise creation ([#2702](https://github.com/axios/axios/pull/2702))
- Adding "synchronous" and "runWhen" options to interceptors api ([#2702](https://github.com/axios/axios/pull/2702))
- Updating of transformResponse ([#3377](https://github.com/axios/axios/pull/3377))
- Adding ability to omit User-Agent header ([#3703](https://github.com/axios/axios/pull/3703))
- Adding multiple JSON improvements ([#3688](https://github.com/axios/axios/pull/3688), [#3763](https://github.com/axios/axios/pull/3763))
- Fixing quadratic runtime and extra memory usage when setting a maxContentLength ([#3738](https://github.com/axios/axios/pull/3738))
- Adding parseInt to config.timeout ([#3781](https://github.com/axios/axios/pull/3781))
- Adding custom return type support to interceptor ([#3783](https://github.com/axios/axios/pull/3783))
- Adding security fix for ReDoS vulnerability ([#3980](https://github.com/axios/axios/pull/3980))

Internal and Tests:

- Updating build dev dependancies ([#3401](https://github.com/axios/axios/pull/3401))
- Fixing builds running on Travis CI ([#3538](https://github.com/axios/axios/pull/3538))
- Updating follow rediect version ([#3694](https://github.com/axios/axios/pull/3694), [#3771](https://github.com/axios/axios/pull/3771))
- Updating karma sauce launcher to fix failing sauce tests ([#3712](https://github.com/axios/axios/pull/3712), [#3717](https://github.com/axios/axios/pull/3717))
- Updating content-type header for application/json to not contain charset field, according do RFC 8259 ([#2154](https://github.com/axios/axios/pull/2154))
- Fixing tests by bumping karma-sauce-launcher version ([#3813](https://github.com/axios/axios/pull/3813))
- Changing testing process from Travis CI to GitHub Actions ([#3938](https://github.com/axios/axios/pull/3938))

Documentation:

- Updating documentation around the use of `AUTH_TOKEN` with multiple domain endpoints ([#3539](https://github.com/axios/axios/pull/3539))
- Remove duplication of item in changelog ([#3523](https://github.com/axios/axios/pull/3523))
- Fixing gramatical errors ([#2642](https://github.com/axios/axios/pull/2642))
- Fixing spelling error ([#3567](https://github.com/axios/axios/pull/3567))
- Moving gitpod metion ([#2637](https://github.com/axios/axios/pull/2637))
- Adding new axios documentation website link ([#3681](https://github.com/axios/axios/pull/3681), [#3707](https://github.com/axios/axios/pull/3707))
- Updating documentation around dispatching requests ([#3772](https://github.com/axios/axios/pull/3772))
- Adding documentation for the type guard isAxiosError ([#3767](https://github.com/axios/axios/pull/3767))
- Adding explanation of cancel token ([#3803](https://github.com/axios/axios/pull/3803))
- Updating CI status badge ([#3953](https://github.com/axios/axios/pull/3953))
- Fixing errors with JSON documentation ([#3936](https://github.com/axios/axios/pull/3936))
- Fixing README typo under Request Config ([#3825](https://github.com/axios/axios/pull/3825))
- Adding axios-multi-api to the ecosystem file ([#3817](https://github.com/axios/axios/pull/3817))
- Adding SECURITY.md to properly disclose security vulnerabilities ([#3981](https://github.com/axios/axios/pull/3981))

Huge thanks to everyone who contributed to this release via code (authors listed below) or via reviews and triaging on GitHub:

- [Jay](mailto:jasonsaayman@gmail.com)
- [Sasha Korotkov](https://github.com/SashaKoro)
- [Daniel Lopretto](https://github.com/timemachine3030)
- [Mike Bishop](https://github.com/MikeBishop)
- [Dmitriy Mozgovoy](https://github.com/DigitalBrainJS)
- [Mark](https://github.com/bimbiltu)
- [Philipe Gouveia Paixão](https://github.com/piiih)
- [hippo](https://github.com/hippo2cat)
- [ready-research](https://github.com/ready-research)
- [Xianming Zhong](https://github.com/chinesedfan)
- [Christopher Chrapka](https://github.com/OJezu)
- [Brian Anglin](https://github.com/anglinb)
- [Kohta Ito](https://github.com/koh110)
- [Ali Clark](https://github.com/aliclark)
- [caikan](https://github.com/caikan)
- [Elina Gorshkova](https://github.com/elinagorshkova)
- [Ryota Ikezawa](https://github.com/paveg)
- [Nisar Hassan Naqvi](https://github.com/nisarhassan12)
- [Jake](https://github.com/codemaster138)
- [TagawaHirotaka](https://github.com/wafuwafu13)
- [Johannes Jarbratt](https://github.com/johachi)
- [Mo Sattler](https://github.com/MoSattler)
- [Sam Carlton](https://github.com/ThatGuySam)
- [Matt Czapliński](https://github.com/MattCCC)
- [Ziding Zhang](https://github.com/zidingz)

### 0.21.1 (December 21, 2020)

Fixes and Functionality:

- Hotfix: Prevent SSRF ([#3410](https://github.com/axios/axios/pull/3410))
- Protocol not parsed when setting proxy config from env vars ([#3070](https://github.com/axios/axios/pull/3070))
- Updating axios in types to be lower case ([#2797](https://github.com/axios/axios/pull/2797))
- Adding a type guard for `AxiosError` ([#2949](https://github.com/axios/axios/pull/2949))

Internal and Tests:

- Remove the skipping of the `socket` http test ([#3364](https://github.com/axios/axios/pull/3364))
- Use different socket for Win32 test ([#3375](https://github.com/axios/axios/pull/3375))

Huge thanks to everyone who contributed to this release via code (authors listed below) or via reviews and triaging on GitHub:

- Daniel Lopretto <timemachine3030@users.noreply.github.com>
- Jason Kwok <JasonHK@users.noreply.github.com>
- Jay <jasonsaayman@gmail.com>
- Jonathan Foster <jonathan@jonathanfoster.io>
- Remco Haszing <remcohaszing@gmail.com>
- Xianming Zhong <chinesedfan@qq.com>

### 0.21.0 (October 23, 2020)

Fixes and Functionality:

- Fixing requestHeaders.Authorization ([#3287](https://github.com/axios/axios/pull/3287))
- Fixing node types ([#3237](https://github.com/axios/axios/pull/3237))
- Fixing axios.delete ignores config.data ([#3282](https://github.com/axios/axios/pull/3282))
- Revert "Fixing overwrite Blob/File type as Content-Type in browser. (#1773)" ([#3289](https://github.com/axios/axios/pull/3289))
- Fixing an issue that type 'null' and 'undefined' is not assignable to validateStatus when typescript strict option is enabled ([#3200](https://github.com/axios/axios/pull/3200))

Internal and Tests:

- Lock travis to not use node v15 ([#3361](https://github.com/axios/axios/pull/3361))

Documentation:

- Fixing simple typo, existant -> existent ([#3252](https://github.com/axios/axios/pull/3252))
- Fixing typos ([#3309](https://github.com/axios/axios/pull/3309))

Huge thanks to everyone who contributed to this release via code (authors listed below) or via reviews and triaging on GitHub:

- Allan Cruz <57270969+Allanbcruz@users.noreply.github.com>
- George Cheng <Gerhut@GMail.com>
- Jay <jasonsaayman@gmail.com>
- Kevin Kirsche <Kev.Kirsche+GitHub@gmail.com>
- Remco Haszing <remcohaszing@gmail.com>
- Taemin Shin <cprayer13@gmail.com>
- Tim Gates <tim.gates@iress.com>
- Xianming Zhong <chinesedfan@qq.com>

### 0.20.0 (August 20, 2020)

Release of 0.20.0-pre as a full release with no other changes.

### 0.20.0-pre (July 15, 2020)

Fixes and Functionality:

- Fixing response with utf-8 BOM can not parse to json ([#2419](https://github.com/axios/axios/pull/2419))
  - fix: remove byte order marker (UTF-8 BOM) when transform response
  - fix: remove BOM only utf-8
  - test: utf-8 BOM
  - fix: incorrect param name
- Refactor mergeConfig without utils.deepMerge ([#2844](https://github.com/axios/axios/pull/2844))
  - Adding failing test
  - Fixing #2587 default custom config persisting
  - Adding Concat keys and filter duplicates
  - Fixed value from CPE
  - update for review feedbacks
  - no deepMerge
  - only merge between plain objects
  - fix rename
  - always merge config by mergeConfig
  - extract function mergeDeepProperties
  - refactor mergeConfig with all keys, and add special logic for validateStatus
  - add test for resetting headers
  - add lots of tests and fix a bug
  - should not inherit `data`
  - use simple toString
- Fixing overwrite Blob/File type as Content-Type in browser. ([#1773](https://github.com/axios/axios/pull/1773))
- Fixing an issue that type 'null' is not assignable to validateStatus ([#2773](https://github.com/axios/axios/pull/2773))
- Fixing special char encoding ([#1671](https://github.com/axios/axios/pull/1671))
  - removing @ character from replacement list since it is a reserved character
  - Updating buildURL test to not include the @ character
  - Removing console logs
- Fixing password encoding with special characters in basic authentication ([#1492](https://github.com/axios/axios/pull/1492))
  - Fixing password encoding with special characters in basic authentication
  - Adding test to check if password with non-Latin1 characters pass
- Fixing 'Network Error' in react native android ([#1487](https://github.com/axios/axios/pull/1487))
  There is a bug in react native Android platform when using get method. It will trigger a 'Network Error' when passing the requestData which is an empty string to request.send function. So if the requestData is an empty string we can set it to null as well to fix the bug.
- Fixing Cookie Helper with Async Components ([#1105](https://github.com/axios/axios/pull/1105)) ([#1107](https://github.com/axios/axios/pull/1107))
- Fixing 'progressEvent' type ([#2851](https://github.com/axios/axios/pull/2851))
  - Fix 'progressEvent' type
  - Update axios.ts
- Fixing getting local files (file://) failed ([#2470](https://github.com/axios/axios/pull/2470))
  - fix issue #2416, #2396
  - fix Eslint warn
  - Modify judgment conditions
  - add unit test
  - update unit test
  - update unit test
- Allow PURGE method in typings ([#2191](https://github.com/axios/axios/pull/2191))
- Adding option to disable automatic decompression ([#2661](https://github.com/axios/axios/pull/2661))
  - Adding ability to disable auto decompression
  - Updating decompress documentation in README
  - Fixing test\unit\adapters\http.js lint errors
  - Adding test for disabling auto decompression
  - Removing changes that fixed lint errors in tests
  - Removing formatting change to unit test
- Add independent `maxBodyLength` option ([#2781](https://github.com/axios/axios/pull/2781))
  - Add independent option to set the maximum size of the request body
  - Remove maxBodyLength check
  - Update README
  - Assert for error code and message
- Adding responseEncoding to mergeConfig ([#1745](https://github.com/axios/axios/pull/1745))
- Compatible with follow-redirect aborts the request ([#2689](https://github.com/axios/axios/pull/2689))
  - Compatible with follow-redirect aborts the request
  - Use the error code
- Fix merging of params ([#2656](https://github.com/axios/axios/pull/2656))
  - Name function to avoid ESLint func-names warning
  - Switch params config to merge list and update tests
  - Restore testing of both false and null
  - Restore test cases for keys without defaults
  - Include test for non-object values that aren't false-y.
- Revert `finally` as `then` ([#2683](https://github.com/axios/axios/pull/2683))

Internal and Tests:

- Fix stale bot config ([#3049](https://github.com/axios/axios/pull/3049))
  - fix stale bot config
  - fix multiple lines
- Add days and change name to work ([#3035](https://github.com/axios/axios/pull/3035))
- Update close-issues.yml ([#3031](https://github.com/axios/axios/pull/3031))
  - Update close-issues.yml
    Update close message to read better 😄
  - Fix use of quotations
    Use single quotes as per other .yml files
  - Remove user name form message
- Add GitHub actions to close stale issues/prs ([#3029](https://github.com/axios/axios/pull/3029))
  - prepare stale actions
  - update messages
  - Add exempt labels and lighten up comments
- Add GitHub actions to close invalid issues ([#3022](https://github.com/axios/axios/pull/3022))
  - add close actions
  - fix with checkout
  - update issue templates
  - add reminder
  - update close message
- Add test with Node.js 12 ([#2860](https://github.com/axios/axios/pull/2860))
  - test with Node.js 12
  - test with latest
- Adding console log on sandbox server startup ([#2210](https://github.com/axios/axios/pull/2210))
  - Adding console log on sandbox server startup
  - Update server.js
    Add server error handling
  - Update server.js
    Better error message, remove retry.
- Adding tests for method `options` type definitions ([#1996](https://github.com/axios/axios/pull/1996))
  Update tests.
- Add test for redirecting with too large response ([#2695](https://github.com/axios/axios/pull/2695))
- Fixing unit test failure in Windows OS ([#2601](https://github.com/axios/axios/pull/2601))
- Fixing issue for HEAD method and gzipped response ([#2666](https://github.com/axios/axios/pull/2666))
- Fix tests in browsers ([#2748](https://github.com/axios/axios/pull/2748))
- chore: add `jsdelivr` and `unpkg` support ([#2443](https://github.com/axios/axios/pull/2443))

Documentation:

- Adding support for URLSearchParams in node ([#1900](https://github.com/axios/axios/pull/1900))
  - Adding support for URLSearchParams in node
  - Remove un-needed code
  - Update utils.js
  - Make changes as suggested
- Adding table of content (preview) ([#3050](https://github.com/axios/axios/pull/3050))
  - add toc (preview)
  - remove toc in toc
    Signed-off-by: Moni <usmoni@gmail.com>
  - fix sublinks
  - fix indentation
  - remove redundant table links
  - update caps and indent
  - remove axios
- Replace 'blacklist' with 'blocklist' ([#3006](https://github.com/axios/axios/pull/3006))
- docs(): Detailed config options environment. ([#2088](https://github.com/axios/axios/pull/2088))
  - docs(): Detailed config options environment.
  - Update README.md
- Include axios-data-unpacker in ECOSYSTEM.md ([#2080](https://github.com/axios/axios/pull/2080))
- Allow opening examples in Gitpod ([#1958](https://github.com/axios/axios/pull/1958))
- Remove axios.all() and axios.spread() from Readme.md ([#2727](https://github.com/axios/axios/pull/2727))
  - remove axios.all(), axios.spread()
  - replace example
  - axios.all() -> Promise.all()
  - axios.spread(function (acct, perms)) -> function (acct, perms)
  - add deprecated mark
- Update README.md ([#2887](https://github.com/axios/axios/pull/2887))
  Small change to the data attribute doc of the config. A request body can also be set for DELETE methods but this wasn't mentioned in the documentation (it only mentioned POST, PUT and PATCH). Took my some 10-20 minutes until I realized that I don't need to manipulate the request body with transformRequest in the case of DELETE.
- Include swagger-taxos-codegen in ECOSYSTEM.md ([#2162](https://github.com/axios/axios/pull/2162))
- Add CDNJS version badge in README.md ([#878](https://github.com/axios/axios/pull/878))
  This badge will show the version on CDNJS!
- Documentation update to clear up ambiguity in code examples ([#2928](https://github.com/axios/axios/pull/2928))
  - Made an adjustment to the documentation to clear up any ambiguity around the use of "fs". This should help clear up that the code examples with "fs" cannot be used on the client side.
- Update README.md about validateStatus ([#2912](https://github.com/axios/axios/pull/2912))
  Rewrote the comment from "Reject only if the status code is greater than or equal to 500" to "Resolve only if the status code is less than 500"
- Updating documentation for usage form-data ([#2805](https://github.com/axios/axios/pull/2805))
  Closes #2049
- Fixing CHANGELOG.md issue link ([#2784](https://github.com/axios/axios/pull/2784))
- Include axios-hooks in ECOSYSTEM.md ([#2003](https://github.com/axios/axios/pull/2003))
- Added Response header access instructions ([#1901](https://github.com/axios/axios/pull/1901))
  - Added Response header access instructions
  - Added note about using bracket notation
- Add `onUploadProgress` and `onDownloadProgress` are browser only ([#2763](https://github.com/axios/axios/pull/2763))
  Saw in #928 and #1966 that `onUploadProgress` and `onDownloadProgress` only work in the browser and was missing that from the README.
- Update ' sign to ` in proxy spec ([#2778](https://github.com/axios/axios/pull/2778))
- Adding jsDelivr link in README ([#1110](https://github.com/axios/axios/pull/1110))
  - Adding jsDelivr link
  - Add SRI
  - Remove SRI

Huge thanks to everyone who contributed to this release via code (authors listed
below) or via reviews and triaging on GitHub:

- Alan Wang <wp_scut@163.com>
- Alexandru Ungureanu <khakcarot@gmail.com>
- Anubhav Srivastava <anubhav.srivastava00@gmail.com>
- Benny Neugebauer <bn@bennyn.de>
- Cr <631807682@qq.com>
- David <cygnidavid@gmail.com>
- David Ko <david.ko@pvtmethod.com>
- David Tanner <david.tanner@lifeomic.com>
- Emily Morehouse <emilyemorehouse@gmail.com>
- Felipe Martins <felipewmartins@gmail.com>
- Fonger <5862369+Fonger@users.noreply.github.com>
- Frostack <soulburn007@gmail.com>
- George Cheng <Gerhut@GMail.com>
- grumblerchester <grumblerchester@users.noreply.github.com>
- Gustavo López <gualopezb@gmail.com>
- hexaez <45806662+hexaez@users.noreply.github.com>
- huangzuizui <huangzuizui@gmail.com>
- Ian Wijma <ian@wij.ma>
- Jay <jasonsaayman@gmail.com>
- jeffjing <zgayjjf@qq.com>
- jennynju <46782518+jennynju@users.noreply.github.com>
- Jimmy Liao <52391190+jimmy-liao-gogoro@users.noreply.github.com>
- Jonathan Sharpe <j.r.sharpe@gmail.com>
- JounQin <admin@1stg.me>
- Justin Beckwith <justin.beckwith@gmail.com>
- Kamil Posiadała <3dcreator.pl@gmail.com>
- Lukas Drgon <lukas.drgon@gmail.com>
- marcinx <mail@marcinx.com>
- Martti Laine <martti@codeclown.net>
- Michał Zarach <michal.m.zarach@gmail.com>
- Moni <usmoni@gmail.com>
- Motonori Iwata <121048+iwata@users.noreply.github.com>
- Nikita Galkin <nikita@galk.in>
- Petr Mares <petr@mares.tw>
- Philippe Recto <precto1285@gmal.com>
- Remco Haszing <remcohaszing@gmail.com>
- rockcs1992 <chengshi1219@gmail.com>
- Ryan Bown <rbown@niftee.com.au>
- Samina Fu <sufuf3@gmail.com>
- Simone Busoli <simone.busoli@gmail.com>
- Spencer von der Ohe <s.vonderohe40@gmail.com>
- Sven Efftinge <sven.efftinge@typefox.io>
- Taegyeoung Oh <otk1090@naver.com>
- Taemin Shin <cprayer13@gmail.com>
- Thibault Ehrhart <1208424+ehrhart@users.noreply.github.com>
- Xianming Zhong <chinesedfan@qq.com>
- Yasu Flores <carlosyasu91@gmail.com>
- Zac Delventhal <delventhalz@gmail.com>

### 0.19.2 (Jan 20, 2020)

- Remove unnecessary XSS check ([#2679](https://github.com/axios/axios/pull/2679)) (see ([#2646](https://github.com/axios/axios/issues/2646)) for discussion)

### 0.19.1 (Jan 7, 2020)

Fixes and Functionality:

- Fixing invalid agent issue ([#1904](https://github.com/axios/axios/pull/1904))
- Fix ignore set withCredentials false ([#2582](https://github.com/axios/axios/pull/2582))
- Delete useless default to hash ([#2458](https://github.com/axios/axios/pull/2458))
- Fix HTTP/HTTPs agents passing to follow-redirect ([#1904](https://github.com/axios/axios/pull/1904))
- Fix ignore set withCredentials false ([#2582](https://github.com/axios/axios/pull/2582))
- Fix CI build failure ([#2570](https://github.com/axios/axios/pull/2570))
- Remove dependency on is-buffer from package.json ([#1816](https://github.com/axios/axios/pull/1816))
- Adding options typings ([#2341](https://github.com/axios/axios/pull/2341))
- Adding Typescript HTTP method definition for LINK and UNLINK. ([#2444](https://github.com/axios/axios/pull/2444))
- Update dist with newest changes, fixes Custom Attributes issue
- Change syntax to see if build passes ([#2488](https://github.com/axios/axios/pull/2488))
- Update Webpack + deps, remove now unnecessary polyfills ([#2410](https://github.com/axios/axios/pull/2410))
- Fix to prevent XSS, throw an error when the URL contains a JS script ([#2464](https://github.com/axios/axios/pull/2464))
- Add custom timeout error copy in config ([#2275](https://github.com/axios/axios/pull/2275))
- Add error toJSON example ([#2466](https://github.com/axios/axios/pull/2466))
- Fixing Vulnerability A Fortify Scan finds a critical Cross-Site Scrip… ([#2451](https://github.com/axios/axios/pull/2451))
- Fixing subdomain handling on no_proxy ([#2442](https://github.com/axios/axios/pull/2442))
- Make redirection from HTTP to HTTPS work ([#2426](https://github.com/axios/axios/pull/2426)) and ([#2547](https://github.com/axios/axios/pull/2547))
- Add toJSON property to AxiosError type ([#2427](https://github.com/axios/axios/pull/2427))
- Fixing socket hang up error on node side for slow response. ([#1752](https://github.com/axios/axios/pull/1752))
- Alternative syntax to send data into the body ([#2317](https://github.com/axios/axios/pull/2317))
- Fixing custom config options ([#2207](https://github.com/axios/axios/pull/2207))
- Fixing set `config.method` after mergeConfig for Axios.prototype.request ([#2383](https://github.com/axios/axios/pull/2383))
- Axios create url bug ([#2290](https://github.com/axios/axios/pull/2290))
- Do not modify config.url when using a relative baseURL (resolves [#1628](https://github.com/axios/axios/issues/1098)) ([#2391](https://github.com/axios/axios/pull/2391))

Internal:

- Revert "Update Webpack + deps, remove now unnecessary polyfills" ([#2479](https://github.com/axios/axios/pull/2479))
- Order of if/else blocks is causing unit tests mocking XHR. ([#2201](https://github.com/axios/axios/pull/2201))
- Add license badge ([#2446](https://github.com/axios/axios/pull/2446))
- Fix travis CI build [#2386](https://github.com/axios/axios/pull/2386)
- Fix cancellation error on build master. #2290 #2207 ([#2407](https://github.com/axios/axios/pull/2407))

Documentation:

- Fixing typo in CHANGELOG.md: s/Functionallity/Functionality ([#2639](https://github.com/axios/axios/pull/2639))
- Fix badge, use master branch ([#2538](https://github.com/axios/axios/pull/2538))
- Fix typo in changelog [#2193](https://github.com/axios/axios/pull/2193)
- Document fix ([#2514](https://github.com/axios/axios/pull/2514))
- Update docs with no_proxy change, issue #2484 ([#2513](https://github.com/axios/axios/pull/2513))
- Fixing missing words in docs template ([#2259](https://github.com/axios/axios/pull/2259))
- 🐛Fix request finally documentation in README ([#2189](https://github.com/axios/axios/pull/2189))
- updating spelling and adding link to docs ([#2212](https://github.com/axios/axios/pull/2212))
- docs: minor tweak ([#2404](https://github.com/axios/axios/pull/2404))
- Update response interceptor docs ([#2399](https://github.com/axios/axios/pull/2399))
- Update README.md ([#2504](https://github.com/axios/axios/pull/2504))
- Fix word 'sintaxe' to 'syntax' in README.md ([#2432](https://github.com/axios/axios/pull/2432))
- updating README: notes on CommonJS autocomplete ([#2256](https://github.com/axios/axios/pull/2256))
- Fix grammar in README.md ([#2271](https://github.com/axios/axios/pull/2271))
- Doc fixes, minor examples cleanup ([#2198](https://github.com/axios/axios/pull/2198))

### 0.19.0 (May 30, 2019)

Fixes and Functionality:

- Added support for no_proxy env variable ([#1693](https://github.com/axios/axios/pull/1693/files)) - Chance Dickson
- Unzip response body only for statuses != 204 ([#1129](https://github.com/axios/axios/pull/1129)) - drawski
- Destroy stream on exceeding maxContentLength (fixes [#1098](https://github.com/axios/axios/issues/1098)) ([#1485](https://github.com/axios/axios/pull/1485)) - Gadzhi Gadzhiev
- Makes Axios error generic to use AxiosResponse ([#1738](https://github.com/axios/axios/pull/1738)) - Suman Lama
- Fixing Mocha tests by locking follow-redirects version to 1.5.10 ([#1993](https://github.com/axios/axios/pull/1993)) - grumblerchester
- Allow uppercase methods in typings. ([#1781](https://github.com/axios/axios/pull/1781)) - Ken Powers
- Fixing building url with hash mark ([#1771](https://github.com/axios/axios/pull/1771)) - Anatoly Ryabov
- This commit fix building url with hash map (fragment identifier) when parameters are present: they must not be added after `#`, because client cut everything after `#`
- Preserve HTTP method when following redirect ([#1758](https://github.com/axios/axios/pull/1758)) - Rikki Gibson
- Add `getUri` signature to TypeScript definition. ([#1736](https://github.com/axios/axios/pull/1736)) - Alexander Trauzzi
- Adding isAxiosError flag to errors thrown by axios ([#1419](https://github.com/axios/axios/pull/1419)) - Ayush Gupta

Internal:

- Fixing .eslintrc without extension ([#1789](https://github.com/axios/axios/pull/1789)) - Manoel
- Fix failing SauceLabs tests by updating configuration - Emily Morehouse
- Add issue templates - Emily Morehouse

Documentation:

- Consistent coding style in README ([#1787](https://github.com/axios/axios/pull/1787)) - Ali Servet Donmez
- Add information about auth parameter to README ([#2166](https://github.com/axios/axios/pull/2166)) - xlaguna
- Add DELETE to list of methods that allow data as a config option ([#2169](https://github.com/axios/axios/pull/2169)) - Daniela Borges Matos de Carvalho
- Update ECOSYSTEM.md - Add Axios Endpoints ([#2176](https://github.com/axios/axios/pull/2176)) - Renan
- Add r2curl in ECOSYSTEM ([#2141](https://github.com/axios/axios/pull/2141)) - 유용우 / CX
- Update README.md - Add instructions for installing with yarn ([#2036](https://github.com/axios/axios/pull/2036)) - Victor Hermes
- Fixing spacing for README.md ([#2066](https://github.com/axios/axios/pull/2066)) - Josh McCarty
- Update README.md. - Change `.then` to `.finally` in example code ([#2090](https://github.com/axios/axios/pull/2090)) - Omar Cai
- Clarify what values responseType can have in Node ([#2121](https://github.com/axios/axios/pull/2121)) - Tyler Breisacher
- docs(ECOSYSTEM): add axios-api-versioning ([#2020](https://github.com/axios/axios/pull/2020)) - Weffe
- It seems that `responseType: 'blob'` doesn't actually work in Node (when I tried using it, response.data was a string, not a Blob, since Node doesn't have Blobs), so this clarifies that this option should only be used in the browser
- Update README.md. - Add Querystring library note ([#1896](https://github.com/axios/axios/pull/1896)) - Dmitriy Eroshenko
- Add react-hooks-axios to Libraries section of ECOSYSTEM.md ([#1925](https://github.com/axios/axios/pull/1925)) - Cody Chan
- Clarify in README that default timeout is 0 (no timeout) ([#1750](https://github.com/axios/axios/pull/1750)) - Ben Standefer

### 0.19.0-beta.1 (Aug 9, 2018)

**NOTE:** This is a beta version of this release. There may be functionality that is broken in
certain browsers, though we suspect that builds are hanging and not erroring. See
https://saucelabs.com/u/axios for the most up-to-date information.

New Functionality:

- Add getUri method ([#1712](https://github.com/axios/axios/issues/1712))
- Add support for no_proxy env variable ([#1693](https://github.com/axios/axios/issues/1693))
- Add toJSON to decorated Axios errors to facilitate serialization ([#1625](https://github.com/axios/axios/issues/1625))
- Add second then on axios call ([#1623](https://github.com/axios/axios/issues/1623))
- Typings: allow custom return types
- Add option to specify character set in responses (with http adapter)

Fixes:

- Fix Keep defaults local to instance ([#385](https://github.com/axios/axios/issues/385))
- Correctly catch exception in http test ([#1475](https://github.com/axios/axios/issues/1475))
- Fix accept header normalization ([#1698](https://github.com/axios/axios/issues/1698))
- Fix http adapter to allow HTTPS connections via HTTP ([#959](https://github.com/axios/axios/issues/959))
- Fix Removes usage of deprecated Buffer constructor. ([#1555](https://github.com/axios/axios/issues/1555), [#1622](https://github.com/axios/axios/issues/1622))
- Fix defaults to use httpAdapter if available ([#1285](https://github.com/axios/axios/issues/1285))
  - Fixing defaults to use httpAdapter if available
  - Use a safer, cross-platform method to detect the Node environment
- Fix Reject promise if request is cancelled by the browser ([#537](https://github.com/axios/axios/issues/537))
- [Typescript] Fix missing type parameters on delete/head methods
- [NS]: Send `false` flag isStandardBrowserEnv for Nativescript
- Fix missing type parameters on delete/head
- Fix Default method for an instance always overwritten by get
- Fix type error when socketPath option in AxiosRequestConfig
- Capture errors on request data streams
- Decorate resolve and reject to clear timeout in all cases

Huge thanks to everyone who contributed to this release via code (authors listed
below) or via reviews and triaging on GitHub:

- Andrew Scott <ascott18@gmail.com>
- Anthony Gauthier <antho325@hotmail.com>
- arpit <arpit2438735@gmail.com>
- ascott18
- Benedikt Rötsch <axe312ger@users.noreply.github.com>
- Chance Dickson <me@chancedickson.com>
- Dave Stewart <info@davestewart.co.uk>
- Deric Cain <deric.cain@gmail.com>
- Guillaume Briday <guillaumebriday@gmail.com>
- Jacob Wejendorp <jacob@wejendorp.dk>
- Jim Lynch <mrdotjim@gmail.com>
- johntron
- Justin Beckwith <beckwith@google.com>
- Justin Beckwith <justin.beckwith@gmail.com>
- Khaled Garbaya <khaledgarbaya@gmail.com>
- Lim Jing Rong <jjingrong@users.noreply.github.com>
- Mark van den Broek <mvdnbrk@gmail.com>
- Martti Laine <martti@codeclown.net>
- mattridley
- mattridley <matt.r@joinblink.com>
- Nicolas Del Valle <nicolas.delvalle@gmail.com>
- Nilegfx
- pbarbiero
- Rikki Gibson <rikkigibson@gmail.com>
- Sako Hartounian <sakohartounian@yahoo.com>
- Shane Fitzpatrick <fitzpasd@gmail.com>
- Stephan Schneider <stephanschndr@gmail.com>
- Steven <steven@ceriously.com>
- Tim Garthwaite <tim.garthwaite@jibo.com>
- Tim Johns <timjohns@yahoo.com>
- Yutaro Miyazaki <yutaro@studio-rubbish.com>

### 0.18.0 (Feb 19, 2018)

- Adding support for UNIX Sockets when running with Node.js ([#1070](https://github.com/axios/axios/pull/1070))
- Fixing typings ([#1177](https://github.com/axios/axios/pull/1177)):
  - AxiosRequestConfig.proxy: allows type false
  - AxiosProxyConfig: added auth field
- Adding function signature in AxiosInstance interface so AxiosInstance can be invoked ([#1192](https://github.com/axios/axios/pull/1192), [#1254](https://github.com/axios/axios/pull/1254))
- Allowing maxContentLength to pass through to redirected calls as maxBodyLength in follow-redirects config ([#1287](https://github.com/axios/axios/pull/1287))
- Fixing configuration when using an instance - method can now be set ([#1342](https://github.com/axios/axios/pull/1342))

### 0.17.1 (Nov 11, 2017)

- Fixing issue with web workers ([#1160](https://github.com/axios/axios/pull/1160))
- Allowing overriding transport ([#1080](https://github.com/axios/axios/pull/1080))
- Updating TypeScript typings ([#1165](https://github.com/axios/axios/pull/1165), [#1125](https://github.com/axios/axios/pull/1125), [#1131](https://github.com/axios/axios/pull/1131))

### 0.17.0 (Oct 21, 2017)

- **BREAKING** Fixing issue with `baseURL` and interceptors ([#950](https://github.com/axios/axios/pull/950))
- **BREAKING** Improving handing of duplicate headers ([#874](https://github.com/axios/axios/pull/874))
- Adding support for disabling proxies ([#691](https://github.com/axios/axios/pull/691))
- Updating TypeScript typings with generic type parameters ([#1061](https://github.com/axios/axios/pull/1061))

### 0.16.2 (Jun 3, 2017)

- Fixing issue with including `buffer` in bundle ([#887](https://github.com/axios/axios/pull/887))
- Including underlying request in errors ([#830](https://github.com/axios/axios/pull/830))
- Convert `method` to lowercase ([#930](https://github.com/axios/axios/pull/930))

### 0.16.1 (Apr 8, 2017)

- Improving HTTP adapter to return last request in case of redirects ([#828](https://github.com/axios/axios/pull/828))
- Updating `follow-redirects` dependency ([#829](https://github.com/axios/axios/pull/829))
- Adding support for passing `Buffer` in node ([#773](https://github.com/axios/axios/pull/773))

### 0.16.0 (Mar 31, 2017)

- **BREAKING** Removing `Promise` from axios typings in favor of built-in type declarations ([#480](https://github.com/axios/axios/issues/480))
- Adding `options` shortcut method ([#461](https://github.com/axios/axios/pull/461))
- Fixing issue with using `responseType: 'json'` in browsers incompatible with XHR Level 2 ([#654](https://github.com/axios/axios/pull/654))
- Improving React Native detection ([#731](https://github.com/axios/axios/pull/731))
- Fixing `combineURLs` to support empty `relativeURL` ([#581](https://github.com/axios/axios/pull/581))
- Removing `PROTECTION_PREFIX` support ([#561](https://github.com/axios/axios/pull/561))

### 0.15.3 (Nov 27, 2016)

- Fixing issue with custom instances and global defaults ([#443](https://github.com/axios/axios/issues/443))
- Renaming `axios.d.ts` to `index.d.ts` ([#519](https://github.com/axios/axios/issues/519))
- Adding `get`, `head`, and `delete` to `defaults.headers` ([#509](https://github.com/axios/axios/issues/509))
- Fixing issue with `btoa` and IE ([#507](https://github.com/axios/axios/issues/507))
- Adding support for proxy authentication ([#483](https://github.com/axios/axios/pull/483))
- Improving HTTP adapter to use `http` protocol by default ([#493](https://github.com/axios/axios/pull/493))
- Fixing proxy issues ([#491](https://github.com/axios/axios/pull/491))

### 0.15.2 (Oct 17, 2016)

- Fixing issue with calling `cancel` after response has been received ([#482](https://github.com/axios/axios/issues/482))

### 0.15.1 (Oct 14, 2016)

- Fixing issue with UMD ([#485](https://github.com/axios/axios/issues/485))

### 0.15.0 (Oct 10, 2016)

- Adding cancellation support ([#452](https://github.com/axios/axios/pull/452))
- Moving default adapter to global defaults ([#437](https://github.com/axios/axios/pull/437))
- Fixing issue with `file` URI scheme ([#440](https://github.com/axios/axios/pull/440))
- Fixing issue with `params` objects that have no prototype ([#445](https://github.com/axios/axios/pull/445))

### 0.14.0 (Aug 27, 2016)

- **BREAKING** Updating TypeScript definitions ([#419](https://github.com/axios/axios/pull/419))
- **BREAKING** Replacing `agent` option with `httpAgent` and `httpsAgent` ([#387](https://github.com/axios/axios/pull/387))
- **BREAKING** Splitting `progress` event handlers into `onUploadProgress` and `onDownloadProgress` ([#423](https://github.com/axios/axios/pull/423))
- Adding support for `http_proxy` and `https_proxy` environment variables ([#366](https://github.com/axios/axios/pull/366))
- Fixing issue with `auth` config option and `Authorization` header ([#397](https://github.com/axios/axios/pull/397))
- Don't set XSRF header if `xsrfCookieName` is `null` ([#406](https://github.com/axios/axios/pull/406))

### 0.13.1 (Jul 16, 2016)

- Fixing issue with response data not being transformed on error ([#378](https://github.com/axios/axios/issues/378))

### 0.13.0 (Jul 13, 2016)

- **BREAKING** Improved error handling ([#345](https://github.com/axios/axios/pull/345))
- **BREAKING** Response transformer now invoked in dispatcher not adapter ([10eb238](https://github.com/axios/axios/commit/10eb23865101f9347570552c04e9d6211376e25e))
- **BREAKING** Request adapters now return a `Promise` ([157efd5](https://github.com/axios/axios/commit/157efd5615890301824e3121cc6c9d2f9b21f94a))
- Fixing issue with `withCredentials` not being overwritten ([#343](https://github.com/axios/axios/issues/343))
- Fixing regression with request transformer being called before request interceptor ([#352](https://github.com/axios/axios/issues/352))
- Fixing custom instance defaults ([#341](https://github.com/axios/axios/issues/341))
- Fixing instances created from `axios.create` to have same API as default axios ([#217](https://github.com/axios/axios/issues/217))

### 0.12.0 (May 31, 2016)

- Adding support for `URLSearchParams` ([#317](https://github.com/axios/axios/pull/317))
- Adding `maxRedirects` option ([#307](https://github.com/axios/axios/pull/307))

### 0.11.1 (May 17, 2016)

- Fixing IE CORS support ([#313](https://github.com/axios/axios/pull/313))
- Fixing detection of `FormData` ([#325](https://github.com/axios/axios/pull/325))
- Adding `Axios` class to exports ([#321](https://github.com/axios/axios/pull/321))

### 0.11.0 (Apr 26, 2016)

- Adding support for Stream with HTTP adapter ([#296](https://github.com/axios/axios/pull/296))
- Adding support for custom HTTP status code error ranges ([#308](https://github.com/axios/axios/pull/308))
- Fixing issue with ArrayBuffer ([#299](https://github.com/axios/axios/pull/299))

### 0.10.0 (Apr 20, 2016)

- Fixing issue with some requests sending `undefined` instead of `null` ([#250](https://github.com/axios/axios/pull/250))
- Fixing basic auth for HTTP adapter ([#252](https://github.com/axios/axios/pull/252))
- Fixing request timeout for XHR adapter ([#227](https://github.com/axios/axios/pull/227))
- Fixing IE8 support by using `onreadystatechange` instead of `onload` ([#249](https://github.com/axios/axios/pull/249))
- Fixing IE9 cross domain requests ([#251](https://github.com/axios/axios/pull/251))
- Adding `maxContentLength` option ([#275](https://github.com/axios/axios/pull/275))
- Fixing XHR support for WebWorker environment ([#279](https://github.com/axios/axios/pull/279))
- Adding request instance to response ([#200](https://github.com/axios/axios/pull/200))

### 0.9.1 (Jan 24, 2016)

- Improving handling of request timeout in node ([#124](https://github.com/axios/axios/issues/124))
- Fixing network errors not rejecting ([#205](https://github.com/axios/axios/pull/205))
- Fixing issue with IE rejecting on HTTP 204 ([#201](https://github.com/axios/axios/issues/201))
- Fixing host/port when following redirects ([#198](https://github.com/axios/axios/pull/198))

### 0.9.0 (Jan 18, 2016)

- Adding support for custom adapters
- Fixing Content-Type header being removed when data is false ([#195](https://github.com/axios/axios/pull/195))
- Improving XDomainRequest implementation ([#185](https://github.com/axios/axios/pull/185))
- Improving config merging and order of precedence ([#183](https://github.com/axios/axios/pull/183))
- Fixing XDomainRequest support for only <= IE9 ([#182](https://github.com/axios/axios/pull/182))

### 0.8.1 (Dec 14, 2015)

- Adding support for passing XSRF token for cross domain requests when using `withCredentials` ([#168](https://github.com/axios/axios/pull/168))
- Fixing error with format of basic auth header ([#178](https://github.com/axios/axios/pull/173))
- Fixing error with JSON payloads throwing `InvalidStateError` in some cases ([#174](https://github.com/axios/axios/pull/174))

### 0.8.0 (Dec 11, 2015)

- Adding support for creating instances of axios ([#123](https://github.com/axios/axios/pull/123))
- Fixing http adapter to use `Buffer` instead of `String` in case of `responseType === 'arraybuffer'` ([#128](https://github.com/axios/axios/pull/128))
- Adding support for using custom parameter serializer with `paramsSerializer` option ([#121](https://github.com/axios/axios/pull/121))
- Fixing issue in IE8 caused by `forEach` on `arguments` ([#127](https://github.com/axios/axios/pull/127))
- Adding support for following redirects in node ([#146](https://github.com/axios/axios/pull/146))
- Adding support for transparent decompression if `content-encoding` is set ([#149](https://github.com/axios/axios/pull/149))
- Adding support for transparent XDomainRequest to handle cross domain requests in IE9 ([#140](https://github.com/axios/axios/pull/140))
- Adding support for HTTP basic auth via Authorization header ([#167](https://github.com/axios/axios/pull/167))
- Adding support for baseURL option ([#160](https://github.com/axios/axios/pull/160))

### 0.7.0 (Sep 29, 2015)

- Fixing issue with minified bundle in IE8 ([#87](https://github.com/axios/axios/pull/87))
- Adding support for passing agent in node ([#102](https://github.com/axios/axios/pull/102))
- Adding support for returning result from `axios.spread` for chaining ([#106](https://github.com/axios/axios/pull/106))
- Fixing typescript definition ([#105](https://github.com/axios/axios/pull/105))
- Fixing default timeout config for node ([#112](https://github.com/axios/axios/pull/112))
- Adding support for use in web workers, and react-native ([#70](https://github.com/axios/axios/issue/70)), ([#98](https://github.com/axios/axios/pull/98))
- Adding support for fetch like API `axios(url[, config])` ([#116](https://github.com/axios/axios/issues/116))

### 0.6.0 (Sep 21, 2015)

- Removing deprecated success/error aliases
- Fixing issue with array params not being properly encoded ([#49](https://github.com/axios/axios/pull/49))
- Fixing issue with User-Agent getting overridden ([#69](https://github.com/axios/axios/issues/69))
- Adding support for timeout config ([#56](https://github.com/axios/axios/issues/56))
- Removing es6-promise dependency
- Fixing issue preventing `length` to be used as a parameter ([#91](https://github.com/axios/axios/pull/91))
- Fixing issue with IE8 ([#85](https://github.com/axios/axios/pull/85))
- Converting build to UMD

### 0.5.4 (Apr 08, 2015)

- Fixing issue with FormData not being sent ([#53](https://github.com/axios/axios/issues/53))

### 0.5.3 (Apr 07, 2015)

- Using JSON.parse unconditionally when transforming response string ([#55](https://github.com/axios/axios/issues/55))

### 0.5.2 (Mar 13, 2015)

- Adding support for `statusText` in response ([#46](https://github.com/axios/axios/issues/46))

### 0.5.1 (Mar 10, 2015)

- Fixing issue using strict mode ([#45](https://github.com/axios/axios/issues/45))
- Fixing issue with standalone build ([#47](https://github.com/axios/axios/issues/47))

### 0.5.0 (Jan 23, 2015)

- Adding support for intercepetors ([#14](https://github.com/axios/axios/issues/14))
- Updating es6-promise dependency

### 0.4.2 (Dec 10, 2014)

- Fixing issue with `Content-Type` when using `FormData` ([#22](https://github.com/axios/axios/issues/22))
- Adding support for TypeScript ([#25](https://github.com/axios/axios/issues/25))
- Fixing issue with standalone build ([#29](https://github.com/axios/axios/issues/29))
- Fixing issue with verbs needing to be capitalized in some browsers ([#30](https://github.com/axios/axios/issues/30))

### 0.4.1 (Oct 15, 2014)

- Adding error handling to request for node.js ([#18](https://github.com/axios/axios/issues/18))

### 0.4.0 (Oct 03, 2014)

- Adding support for `ArrayBuffer` and `ArrayBufferView` ([#10](https://github.com/axios/axios/issues/10))
- Adding support for utf-8 for node.js ([#13](https://github.com/axios/axios/issues/13))
- Adding support for SSL for node.js ([#12](https://github.com/axios/axios/issues/12))
- Fixing incorrect `Content-Type` header ([#9](https://github.com/axios/axios/issues/9))
- Adding standalone build without bundled es6-promise ([#11](https://github.com/axios/axios/issues/11))
- Deprecating `success`/`error` in favor of `then`/`catch`

### 0.3.1 (Sep 16, 2014)

- Fixing missing post body when using node.js ([#3](https://github.com/axios/axios/issues/3))

### 0.3.0 (Sep 16, 2014)

- Fixing `success` and `error` to properly receive response data as individual arguments ([#8](https://github.com/axios/axios/issues/8))
- Updating `then` and `catch` to receive response data as a single object ([#6](https://github.com/axios/axios/issues/6))
- Fixing issue with `all` not working ([#7](https://github.com/axios/axios/issues/7))

### 0.2.2 (Sep 14, 2014)

- Fixing bundling with browserify ([#4](https://github.com/axios/axios/issues/4))

### 0.2.1 (Sep 12, 2014)

- Fixing build problem causing ridiculous file sizes

### 0.2.0 (Sep 12, 2014)

- Adding support for `all` and `spread`
- Adding support for node.js ([#1](https://github.com/axios/axios/issues/1))

### 0.1.0 (Aug 29, 2014)

- Initial release

```

### node_modules\axios\README.md
```markdown
# axios

[![npm version](https://img.shields.io/npm/v/axios.svg?style=flat-square)](https://www.npmjs.org/package/axios)
[![CDNJS](https://img.shields.io/cdnjs/v/axios.svg?style=flat-square)](https://cdnjs.com/libraries/axios)
![Build status](https://github.com/axios/axios/actions/workflows/ci.yml/badge.svg)
[![Gitpod Ready-to-Code](https://img.shields.io/badge/Gitpod-Ready--to--Code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/axios/axios) 
[![code coverage](https://img.shields.io/coveralls/mzabriskie/axios.svg?style=flat-square)](https://coveralls.io/r/mzabriskie/axios)
[![install size](https://packagephobia.now.sh/badge?p=axios)](https://packagephobia.now.sh/result?p=axios)
[![npm downloads](https://img.shields.io/npm/dm/axios.svg?style=flat-square)](http://npm-stat.com/charts.html?package=axios)
[![gitter chat](https://img.shields.io/gitter/room/mzabriskie/axios.svg?style=flat-square)](https://gitter.im/mzabriskie/axios)
[![code helpers](https://www.codetriage.com/axios/axios/badges/users.svg)](https://www.codetriage.com/axios/axios)

Promise based HTTP client for the browser and node.js

> New axios docs website: [click here](https://axios-http.com/)

## Table of Contents

  - [Features](#features)
  - [Browser Support](#browser-support)
  - [Installing](#installing)
  - [Example](#example)
  - [Axios API](#axios-api)
  - [Request method aliases](#request-method-aliases)
  - [Concurrency (Deprecated)](#concurrency-deprecated)
  - [Creating an instance](#creating-an-instance)
  - [Instance methods](#instance-methods)
  - [Request Config](#request-config)
  - [Response Schema](#response-schema)
  - [Config Defaults](#config-defaults)
    - [Global axios defaults](#global-axios-defaults)
    - [Custom instance defaults](#custom-instance-defaults)
    - [Config order of precedence](#config-order-of-precedence)
  - [Interceptors](#interceptors)
  - [Handling Errors](#handling-errors)
  - [Cancellation](#cancellation)
  - [Using application/x-www-form-urlencoded format](#using-applicationx-www-form-urlencoded-format)
    - [Browser](#browser)
    - [Node.js](#nodejs)
      - [Query string](#query-string)
      - [Form data](#form-data)
  - [Semver](#semver)
  - [Promises](#promises)
  - [TypeScript](#typescript)
  - [Resources](#resources)
  - [Credits](#credits)
  - [License](#license)

## Features

- Make [XMLHttpRequests](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest) from the browser
- Make [http](http://nodejs.org/api/http.html) requests from node.js
- Supports the [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) API
- Intercept request and response
- Transform request and response data
- Cancel requests
- Automatic transforms for JSON data
- Client side support for protecting against [XSRF](http://en.wikipedia.org/wiki/Cross-site_request_forgery)

## Browser Support

![Chrome](https://raw.github.com/alrra/browser-logos/master/src/chrome/chrome_48x48.png) | ![Firefox](https://raw.github.com/alrra/browser-logos/master/src/firefox/firefox_48x48.png) | ![Safari](https://raw.github.com/alrra/browser-logos/master/src/safari/safari_48x48.png) | ![Opera](https://raw.github.com/alrra/browser-logos/master/src/opera/opera_48x48.png) | ![Edge](https://raw.github.com/alrra/browser-logos/master/src/edge/edge_48x48.png) | ![IE](https://raw.github.com/alrra/browser-logos/master/src/archive/internet-explorer_9-11/internet-explorer_9-11_48x48.png) |
--- | --- | --- | --- | --- | --- |
Latest ✔ | Latest ✔ | Latest ✔ | Latest ✔ | Latest ✔ | 11 ✔ |

[![Browser Matrix](https://saucelabs.com/open_sauce/build_matrix/axios.svg)](https://saucelabs.com/u/axios)

## Installing

Using npm:

```bash
$ npm install axios
```

Using bower:

```bash
$ bower install axios
```

Using yarn:

```bash
$ yarn add axios
```

Using jsDelivr CDN:

```html
<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
```

Using unpkg CDN:

```html
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>
```

## Example

### note: CommonJS usage
In order to gain the TypeScript typings (for intellisense / autocomplete) while using CommonJS imports with `require()` use the following approach:

```js
const axios = require('axios').default;

// axios.<method> will now provide autocomplete and parameter typings
```

Performing a `GET` request

```js
const axios = require('axios');

// Make a request for a user with a given ID
axios.get('/user?ID=12345')
  .then(function (response) {
    // handle success
    console.log(response);
  })
  .catch(function (error) {
    // handle error
    console.log(error);
  })
  .then(function () {
    // always executed
  });

// Optionally the request above could also be done as
axios.get('/user', {
    params: {
      ID: 12345
    }
  })
  .then(function (response) {
    console.log(response);
  })
  .catch(function (error) {
    console.log(error);
  })
  .then(function () {
    // always executed
  });  

// Want to use async/await? Add the `async` keyword to your outer function/method.
async function getUser() {
  try {
    const response = await axios.get('/user?ID=12345');
    console.log(response);
  } catch (error) {
    console.error(error);
  }
}
```

> **NOTE:** `async/await` is part of ECMAScript 2017 and is not supported in Internet
> Explorer and older browsers, so use with caution.

Performing a `POST` request

```js
axios.post('/user', {
    firstName: 'Fred',
    lastName: 'Flintstone'
  })
  .then(function (response) {
    console.log(response);
  })
  .catch(function (error) {
    console.log(error);
  });
```

Performing multiple concurrent requests

```js
function getUserAccount() {
  return axios.get('/user/12345');
}

function getUserPermissions() {
  return axios.get('/user/12345/permissions');
}

Promise.all([getUserAccount(), getUserPermissions()])
  .then(function (results) {
    const acct = results[0];
    const perm = results[1];
  });
```

## axios API

Requests can be made by passing the relevant config to `axios`.

##### axios(config)

```js
// Send a POST request
axios({
  method: 'post',
  url: '/user/12345',
  data: {
    firstName: 'Fred',
    lastName: 'Flintstone'
  }
});
```

```js
// GET request for remote image in node.js
axios({
  method: 'get',
  url: 'http://bit.ly/2mTM3nY',
  responseType: 'stream'
})
  .then(function (response) {
    response.data.pipe(fs.createWriteStream('ada_lovelace.jpg'))
  });
```

##### axios(url[, config])

```js
// Send a GET request (default method)
axios('/user/12345');
```

### Request method aliases

For convenience aliases have been provided for all supported request methods.

##### axios.request(config)
##### axios.get(url[, config])
##### axios.delete(url[, config])
##### axios.head(url[, config])
##### axios.options(url[, config])
##### axios.post(url[, data[, config]])
##### axios.put(url[, data[, config]])
##### axios.patch(url[, data[, config]])

###### NOTE
When using the alias methods `url`, `method`, and `data` properties don't need to be specified in config.

### Concurrency (Deprecated)
Please use `Promise.all` to replace the below functions.

Helper functions for dealing with concurrent requests.

axios.all(iterable)
axios.spread(callback)

### Creating an instance

You can create a new instance of axios with a custom config.

##### axios.create([config])

```js
const instance = axios.create({
  baseURL: 'https://some-domain.com/api/',
  timeout: 1000,
  headers: {'X-Custom-Header': 'foobar'}
});
```

### Instance methods

The available instance methods are listed below. The specified config will be merged with the instance config.

##### axios#request(config)
##### axios#get(url[, config])
##### axios#delete(url[, config])
##### axios#head(url[, config])
##### axios#options(url[, config])
##### axios#post(url[, data[, config]])
##### axios#put(url[, data[, config]])
##### axios#patch(url[, data[, config]])
##### axios#getUri([config])

## Request Config

These are the available config options for making requests. Only the `url` is required. Requests will default to `GET` if `method` is not specified.

```js
{
  // `url` is the server URL that will be used for the request
  url: '/user',

  // `method` is the request method to be used when making the request
  method: 'get', // default

  // `baseURL` will be prepended to `url` unless `url` is absolute.
  // It can be convenient to set `baseURL` for an instance of axios to pass relative URLs
  // to methods of that instance.
  baseURL: 'https://some-domain.com/api/',

  // `transformRequest` allows changes to the request data before it is sent to the server
  // This is only applicable for request methods 'PUT', 'POST', 'PATCH' and 'DELETE'
  // The last function in the array must return a string or an instance of Buffer, ArrayBuffer,
  // FormData or Stream
  // You may modify the headers object.
  transformRequest: [function (data, headers) {
    // Do whatever you want to transform the data

    return data;
  }],

  // `transformResponse` allows changes to the response data to be made before
  // it is passed to then/catch
  transformResponse: [function (data) {
    // Do whatever you want to transform the data

    return data;
  }],

  // `headers` are custom headers to be sent
  headers: {'X-Requested-With': 'XMLHttpRequest'},

  // `params` are the URL parameters to be sent with the request
  // Must be a plain object or a URLSearchParams object
  params: {
    ID: 12345
  },

  // `paramsSerializer` is an optional function in charge of serializing `params`
  // (e.g. https://www.npmjs.com/package/qs, http://api.jquery.com/jquery.param/)
  paramsSerializer: function (params) {
    return Qs.stringify(params, {arrayFormat: 'brackets'})
  },

  // `data` is the data to be sent as the request body
  // Only applicable for request methods 'PUT', 'POST', 'DELETE , and 'PATCH'
  // When no `transformRequest` is set, must be of one of the following types:
  // - string, plain object, ArrayBuffer, ArrayBufferView, URLSearchParams
  // - Browser only: FormData, File, Blob
  // - Node only: Stream, Buffer
  data: {
    firstName: 'Fred'
  },
  
  // syntax alternative to send data into the body
  // method post
  // only the value is sent, not the key
  data: 'Country=Brasil&City=Belo Horizonte',

  // `timeout` specifies the number of milliseconds before the request times out.
  // If the request takes longer than `timeout`, the request will be aborted.
  timeout: 1000, // default is `0` (no timeout)

  // `withCredentials` indicates whether or not cross-site Access-Control requests
  // should be made using credentials
  withCredentials: false, // default

  // `adapter` allows custom handling of requests which makes testing easier.
  // Return a promise and supply a valid response (see lib/adapters/README.md).
  adapter: function (config) {
    /* ... */
  },

  // `auth` indicates that HTTP Basic auth should be used, and supplies credentials.
  // This will set an `Authorization` header, overwriting any existing
  // `Authorization` custom headers you have set using `headers`.
  // Please note that only HTTP Basic auth is configurable through this parameter.
  // For Bearer tokens and such, use `Authorization` custom headers instead.
  auth: {
    username: 'janedoe',
    password: 's00pers3cret'
  },

  // `responseType` indicates the type of data that the server will respond with
  // options are: 'arraybuffer', 'document', 'json', 'text', 'stream'
  //   browser only: 'blob'
  responseType: 'json', // default

  // `responseEncoding` indicates encoding to use for decoding responses (Node.js only)
  // Note: Ignored for `responseType` of 'stream' or client-side requests
  responseEncoding: 'utf8', // default

  // `xsrfCookieName` is the name of the cookie to use as a value for xsrf token
  xsrfCookieName: 'XSRF-TOKEN', // default

  // `xsrfHeaderName` is the name of the http header that carries the xsrf token value
  xsrfHeaderName: 'X-XSRF-TOKEN', // default

  // `onUploadProgress` allows handling of progress events for uploads
  // browser only
  onUploadProgress: function (progressEvent) {
    // Do whatever you want with the native progress event
  },

  // `onDownloadProgress` allows handling of progress events for downloads
  // browser only
  onDownloadProgress: function (progressEvent) {
    // Do whatever you want with the native progress event
  },

  // `maxContentLength` defines the max size of the http response content in bytes allowed in node.js
  maxContentLength: 2000,

  // `maxBodyLength` (Node only option) defines the max size of the http request content in bytes allowed
  maxBodyLength: 2000,

  // `validateStatus` defines whether to resolve or reject the promise for a given
  // HTTP response status code. If `validateStatus` returns `true` (or is set to `null`
  // or `undefined`), the promise will be resolved; otherwise, the promise will be
  // rejected.
  validateStatus: function (status) {
    return status >= 200 && status < 300; // default
  },

  // `maxRedirects` defines the maximum number of redirects to follow in node.js.
  // If set to 0, no redirects will be followed.
  maxRedirects: 5, // default

  // `socketPath` defines a UNIX Socket to be used in node.js.
  // e.g. '/var/run/docker.sock' to send requests to the docker daemon.
  // Only either `socketPath` or `proxy` can be specified.
  // If both are specified, `socketPath` is used.
  socketPath: null, // default

  // `httpAgent` and `httpsAgent` define a custom agent to be used when performing http
  // and https requests, respectively, in node.js. This allows options to be added like
  // `keepAlive` that are not enabled by default.
  httpAgent: new http.Agent({ keepAlive: true }),
  httpsAgent: new https.Agent({ keepAlive: true }),

  // `proxy` defines the hostname, port, and protocol of the proxy server.
  // You can also define your proxy using the conventional `http_proxy` and
  // `https_proxy` environment variables. If you are using environment variables
  // for your proxy configuration, you can also define a `no_proxy` environment
  // variable as a comma-separated list of domains that should not be proxied.
  // Use `false` to disable proxies, ignoring environment variables.
  // `auth` indicates that HTTP Basic auth should be used to connect to the proxy, and
  // supplies credentials.
  // This will set an `Proxy-Authorization` header, overwriting any existing
  // `Proxy-Authorization` custom headers you have set using `headers`.
  // If the proxy server uses HTTPS, then you must set the protocol to `https`. 
  proxy: {
    protocol: 'https',
    host: '127.0.0.1',
    port: 9000,
    auth: {
      username: 'mikeymike',
      password: 'rapunz3l'
    }
  },

  // `cancelToken` specifies a cancel token that can be used to cancel the request
  // (see Cancellation section below for details)
  cancelToken: new CancelToken(function (cancel) {
  }),

  // `decompress` indicates whether or not the response body should be decompressed 
  // automatically. If set to `true` will also remove the 'content-encoding' header 
  // from the responses objects of all decompressed responses
  // - Node only (XHR cannot turn off decompression)
  decompress: true, // default

  // transitional options for backward compatibility that may be removed in the newer versions
  transitional: {
    // silent JSON parsing mode
    // `true`  - ignore JSON parsing errors and set response.data to null if parsing failed (old behaviour)
    // `false` - throw SyntaxError if JSON parsing failed (Note: responseType must be set to 'json')
    silentJSONParsing: true, // default value for the current Axios version

    // try to parse the response string as JSON even if `responseType` is not 'json'
    forcedJSONParsing: true,
    
    // throw ETIMEDOUT error instead of generic ECONNABORTED on request timeouts
    clarifyTimeoutError: false,
  }
}
```

## Response Schema

The response for a request contains the following information.

```js
{
  // `data` is the response that was provided by the server
  data: {},

  // `status` is the HTTP status code from the server response
  status: 200,

  // `statusText` is the HTTP status message from the server response
  statusText: 'OK',

  // `headers` the HTTP headers that the server responded with
  // All header names are lower cased and can be accessed using the bracket notation.
  // Example: `response.headers['content-type']`
  headers: {},

  // `config` is the config that was provided to `axios` for the request
  config: {},

  // `request` is the request that generated this response
  // It is the last ClientRequest instance in node.js (in redirects)
  // and an XMLHttpRequest instance in the browser
  request: {}
}
```

When using `then`, you will receive the response as follows:

```js
axios.get('/user/12345')
  .then(function (response) {
    console.log(response.data);
    console.log(response.status);
    console.log(response.statusText);
    console.log(response.headers);
    console.log(response.config);
  });
```

When using `catch`, or passing a [rejection callback](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/then) as second parameter of `then`, the response will be available through the `error` object as explained in the [Handling Errors](#handling-errors) section.

## Config Defaults

You can specify config defaults that will be applied to every request.

### Global axios defaults

```js
axios.defaults.baseURL = 'https://api.example.com';

// Important: If axios is used with multiple domains, the AUTH_TOKEN will be sent to all of them.
// See below for an example using Custom instance defaults instead.
axios.defaults.headers.common['Authorization'] = AUTH_TOKEN;

axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
```

### Custom instance defaults

```js
// Set config defaults when creating the instance
const instance = axios.create({
  baseURL: 'https://api.example.com'
});

// Alter defaults after instance has been created
instance.defaults.headers.common['Authorization'] = AUTH_TOKEN;
```

### Config order of precedence

Config will be merged with an order of precedence. The order is library defaults found in [lib/defaults.js](https://github.com/axios/axios/blob/master/lib/defaults.js#L28), then `defaults` property of the instance, and finally `config` argument for the request. The latter will take precedence over the former. Here's an example.

```js
// Create an instance using the config defaults provided by the library
// At this point the timeout config value is `0` as is the default for the library
const instance = axios.create();

// Override timeout default for the library
// Now all requests using this instance will wait 2.5 seconds before timing out
instance.defaults.timeout = 2500;

// Override timeout for this request as it's known to take a long time
instance.get('/longRequest', {
  timeout: 5000
});
```

## Interceptors

You can intercept requests or responses before they are handled by `then` or `catch`.

```js
// Add a request interceptor
axios.interceptors.request.use(function (config) {
    // Do something before request is sent
    return config;
  }, function (error) {
    // Do something with request error
    return Promise.reject(error);
  });

// Add a response interceptor
axios.interceptors.response.use(function (response) {
    // Any status code that lie within the range of 2xx cause this function to trigger
    // Do something with response data
    return response;
  }, function (error) {
    // Any status codes that falls outside the range of 2xx cause this function to trigger
    // Do something with response error
    return Promise.reject(error);
  });
```

If you need to remove an interceptor later you can.

```js
const myInterceptor = axios.interceptors.request.use(function () {/*...*/});
axios.interceptors.request.eject(myInterceptor);
```

You can add interceptors to a custom instance of axios.

```js
const instance = axios.create();
instance.interceptors.request.use(function () {/*...*/});
```

When you add request interceptors, they are presumed to be asynchronous by default. This can cause a delay
in the execution of your axios request when the main thread is blocked (a promise is created under the hood for 
the interceptor and your request gets put on the bottom of the call stack). If your request interceptors are synchronous you can add a flag
to the options object that will tell axios to run the code synchronously and avoid any delays in request execution.

```js
axios.interceptors.request.use(function (config) {
  config.headers.test = 'I am only a header!';
  return config;
}, null, { synchronous: true });
```

If you want to execute a particular interceptor based on a runtime check, 
you can add a `runWhen` function to the options object. The interceptor will not be executed **if and only if** the return
of `runWhen` is `false`. The function will be called with the config
object (don't forget that you can bind your own arguments to it as well.) This can be handy when you have an
asynchronous request interceptor that only needs to run at certain times.

```js
function onGetCall(config) {
  return config.method === 'get';
}
axios.interceptors.request.use(function (config) {
  config.headers.test = 'special get headers';
  return config;
}, null, { runWhen: onGetCall });
```

## Handling Errors

```js
axios.get('/user/12345')
  .catch(function (error) {
    if (error.response) {
      // The request was made and the server responded with a status code
      // that falls out of the range of 2xx
      console.log(error.response.data);
      console.log(error.response.status);
      console.log(error.response.headers);
    } else if (error.request) {
      // The request was made but no response was received
      // `error.request` is an instance of XMLHttpRequest in the browser and an instance of
      // http.ClientRequest in node.js
      console.log(error.request);
    } else {
      // Something happened in setting up the request that triggered an Error
      console.log('Error', error.message);
    }
    console.log(error.config);
  });
```

Using the `validateStatus` config option, you can define HTTP code(s) that should throw an error.

```js
axios.get('/user/12345', {
  validateStatus: function (status) {
    return status < 500; // Resolve only if the status code is less than 500
  }
})
```

Using `toJSON` you get an object with more information about the HTTP error.

```js
axios.get('/user/12345')
  .catch(function (error) {
    console.log(error.toJSON());
  });
```

## Cancellation

You can cancel a request using a *cancel token*.

> The axios cancel token API is based on the withdrawn [cancelable promises proposal](https://github.com/tc39/proposal-cancelable-promises).

You can create a cancel token using the `CancelToken.source` factory as shown below:

```js
const CancelToken = axios.CancelToken;
const source = CancelToken.source();

axios.get('/user/12345', {
  cancelToken: source.token
}).catch(function (thrown) {
  if (axios.isCancel(thrown)) {
    console.log('Request canceled', thrown.message);
  } else {
    // handle error
  }
});

axios.post('/user/12345', {
  name: 'new name'
}, {
  cancelToken: source.token
})

// cancel the request (the message parameter is optional)
source.cancel('Operation canceled by the user.');
```

You can also create a cancel token by passing an executor function to the `CancelToken` constructor:

```js
const CancelToken = axios.CancelToken;
let cancel;

axios.get('/user/12345', {
  cancelToken: new CancelToken(function executor(c) {
    // An executor function receives a cancel function as a parameter
    cancel = c;
  })
});

// cancel the request
cancel();
```

> Note: you can cancel several requests with the same cancel token.
> If a cancellation token is already cancelled at the moment of starting an Axios request, then the request is cancelled immediately, without any attempts to make real request.

## Using application/x-www-form-urlencoded format

By default, axios serializes JavaScript objects to `JSON`. To send data in the `application/x-www-form-urlencoded` format instead, you can use one of the following options.

### Browser

In a browser, you can use the [`URLSearchParams`](https://developer.mozilla.org/en-US/docs/Web/API/URLSearchParams) API as follows:

```js
const params = new URLSearchParams();
params.append('param1', 'value1');
params.append('param2', 'value2');
axios.post('/foo', params);
```

> Note that `URLSearchParams` is not supported by all browsers (see [caniuse.com](http://www.caniuse.com/#feat=urlsearchparams)), but there is a [polyfill](https://github.com/WebReflection/url-search-params) available (make sure to polyfill the global environment).

Alternatively, you can encode data using the [`qs`](https://github.com/ljharb/qs) library:

```js
const qs = require('qs');
axios.post('/foo', qs.stringify({ 'bar': 123 }));
```

Or in another way (ES6),

```js
import qs from 'qs';
const data = { 'bar': 123 };
const options = {
  method: 'POST',
  headers: { 'content-type': 'application/x-www-form-urlencoded' },
  data: qs.stringify(data),
  url,
};
axios(options);
```

### Node.js

#### Query string

In node.js, you can use the [`querystring`](https://nodejs.org/api/querystring.html) module as follows:

```js
const querystring = require('querystring');
axios.post('http://something.com/', querystring.stringify({ foo: 'bar' }));
```

or ['URLSearchParams'](https://nodejs.org/api/url.html#url_class_urlsearchparams) from ['url module'](https://nodejs.org/api/url.html) as follows:

```js
const url = require('url');
const params = new url.URLSearchParams({ foo: 'bar' });
axios.post('http://something.com/', params.toString());
```

You can also use the [`qs`](https://github.com/ljharb/qs) library.

###### NOTE
The `qs` library is preferable if you need to stringify nested objects, as the `querystring` method has known issues with that use case (https://github.com/nodejs/node-v0.x-archive/issues/1665).

#### Form data

In node.js, you can use the [`form-data`](https://github.com/form-data/form-data) library as follows:

```js
const FormData = require('form-data');
 
const form = new FormData();
form.append('my_field', 'my value');
form.append('my_buffer', new Buffer(10));
form.append('my_file', fs.createReadStream('/foo/bar.jpg'));

axios.post('https://example.com', form, { headers: form.getHeaders() })
```

Alternatively, use an interceptor:

```js
axios.interceptors.request.use(config => {
  if (config.data instanceof FormData) {
    Object.assign(config.headers, config.data.getHeaders());
  }
  return config;
});
```

## Semver

Until axios reaches a `1.0` release, breaking changes will be released with a new minor version. For example `0.5.1`, and `0.5.4` will have the same API, but `0.6.0` will have breaking changes.

## Promises

axios depends on a native ES6 Promise implementation to be [supported](http://caniuse.com/promises).
If your environment doesn't support ES6 Promises, you can [polyfill](https://github.com/jakearchibald/es6-promise).

## TypeScript

axios includes [TypeScript](http://typescriptlang.org) definitions and a type guard for axios errors.

```typescript
let user: User = null;
try {
  const { data } = await axios.get('/user?ID=12345');
  user = data.userDetails;
} catch (error) {
  if (axios.isAxiosError(error)) {
    handleAxiosError(error);
  } else {
    handleUnexpectedError(error);
  }
}
```

## Online one-click setup

You can use Gitpod an online IDE(which is free for Open Source) for contributing or running the examples online.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/axios/axios/blob/master/examples/server.js)


## Resources

* [Changelog](https://github.com/axios/axios/blob/master/CHANGELOG.md)
* [Upgrade Guide](https://github.com/axios/axios/blob/master/UPGRADE_GUIDE.md)
* [Ecosystem](https://github.com/axios/axios/blob/master/ECOSYSTEM.md)
* [Contributing Guide](https://github.com/axios/axios/blob/master/CONTRIBUTING.md)
* [Code of Conduct](https://github.com/axios/axios/blob/master/CODE_OF_CONDUCT.md)

## Credits

axios is heavily inspired by the [$http service](https://docs.angularjs.org/api/ng/service/$http) provided in [Angular](https://angularjs.org/). Ultimately axios is an effort to provide a standalone `$http`-like service for use outside of Angular.

## License

[MIT](LICENSE)

```

### node_modules\axios\SECURITY.md
```markdown
# Security Policy

## Reporting a Vulnerability

Please report security issues to jasonsaayman@gmail.com

```

### node_modules\axios\UPGRADE_GUIDE.md
```markdown
# Upgrade Guide

### 0.15.x -> 0.16.0

#### `Promise` Type Declarations

The `Promise` type declarations have been removed from the axios typings in favor of the built-in type declarations. If you use axios in a TypeScript project that targets `ES5`, please make sure to include the `es2015.promise` lib. Please see [this post](https://blog.mariusschulz.com/2016/11/25/typescript-2-0-built-in-type-declarations) for details.

### 0.13.x -> 0.14.0

#### TypeScript Definitions

The axios TypeScript definitions have been updated to match the axios API and use the ES2015 module syntax.

Please use the following `import` statement to import axios in TypeScript:

```typescript
import axios from 'axios';

axios.get('/foo')
  .then(response => console.log(response))
  .catch(error => console.log(error));
```

#### `agent` Config Option

The `agent` config option has been replaced with two new options: `httpAgent` and `httpsAgent`. Please use them instead.

```js
{
  // Define a custom agent for HTTP
  httpAgent: new http.Agent({ keepAlive: true }),
  // Define a custom agent for HTTPS
  httpsAgent: new https.Agent({ keepAlive: true })
}
```

#### `progress` Config Option

The `progress` config option has been replaced with the `onUploadProgress` and `onDownloadProgress` options.

```js
{
  // Define a handler for upload progress events
  onUploadProgress: function (progressEvent) {
    // ...
  },

  // Define a handler for download progress events
  onDownloadProgress: function (progressEvent) {
    // ...
  }
}
```

### 0.12.x -> 0.13.0

The `0.13.0` release contains several changes to custom adapters and error handling.

#### Error Handling

Previous to this release an error could either be a server response with bad status code or an actual `Error`. With this release Promise will always reject with an `Error`. In the case that a response was received, the `Error` will also include the response.

```js
axios.get('/user/12345')
  .catch((error) => {
    console.log(error.message);
    console.log(error.code); // Not always specified
    console.log(error.config); // The config that was used to make the request
    console.log(error.response); // Only available if response was received from the server
  });
```

#### Request Adapters

This release changes a few things about how request adapters work. Please take note if you are using your own custom adapter.

1. Response transformer is now called outside of adapter.
2. Request adapter returns a `Promise`.

This means that you no longer need to invoke `transformData` on response data. You will also no longer receive `resolve` and `reject` as arguments in your adapter.

Previous code:

```js
function myAdapter(resolve, reject, config) {
  var response = {
    data: transformData(
      responseData,
      responseHeaders,
      config.transformResponse
    ),
    status: request.status,
    statusText: request.statusText,
    headers: responseHeaders
  };
  settle(resolve, reject, response);
}
```

New code:

```js
function myAdapter(config) {
  return new Promise(function (resolve, reject) {
    var response = {
      data: responseData,
      status: request.status,
      statusText: request.statusText,
      headers: responseHeaders
    };
    settle(resolve, reject, response);
  });
}
```

See the related commits for more details:
- [Response transformers](https://github.com/axios/axios/commit/10eb23865101f9347570552c04e9d6211376e25e)
- [Request adapter Promise](https://github.com/axios/axios/commit/157efd5615890301824e3121cc6c9d2f9b21f94a)

### 0.5.x -> 0.6.0

The `0.6.0` release contains mostly bug fixes, but there are a couple things to be aware of when upgrading.

#### ES6 Promise Polyfill

Up until the `0.6.0` release ES6 `Promise` was being polyfilled using [es6-promise](https://github.com/jakearchibald/es6-promise). With this release, the polyfill has been removed, and you will need to supply it yourself if your environment needs it.

```js
require('es6-promise').polyfill();
var axios = require('axios');
```

This will polyfill the global environment, and only needs to be done once.

#### `axios.success`/`axios.error`

The `success`, and `error` aliases were deprecated in [0.4.0](https://github.com/axios/axios/blob/master/CHANGELOG.md#040-oct-03-2014). As of this release they have been removed entirely. Instead please use `axios.then`, and `axios.catch` respectively.

```js
axios.get('some/url')
  .then(function (res) {
    /* ... */
  })
  .catch(function (err) {
    /* ... */
  });
```

#### UMD

Previous versions of axios shipped with an AMD, CommonJS, and Global build. This has all been rolled into a single UMD build.

```js
// AMD
require(['bower_components/axios/dist/axios'], function (axios) {
  /* ... */
});

// CommonJS
var axios = require('axios/dist/axios');
```

```

### node_modules\axios\index.d.ts
```typescript
export interface AxiosTransformer {
  (data: any, headers?: any): any;
}

export interface AxiosAdapter {
  (config: AxiosRequestConfig): AxiosPromise<any>;
}

export interface AxiosBasicCredentials {
  username: string;
  password: string;
}

export interface AxiosProxyConfig {
  host: string;
  port: number;
  auth?: {
    username: string;
    password:string;
  };
  protocol?: string;
}

export type Method =
  | 'get' | 'GET'
  | 'delete' | 'DELETE'
  | 'head' | 'HEAD'
  | 'options' | 'OPTIONS'
  | 'post' | 'POST'
  | 'put' | 'PUT'
  | 'patch' | 'PATCH'
  | 'purge' | 'PURGE'
  | 'link' | 'LINK'
  | 'unlink' | 'UNLINK'

export type ResponseType =
  | 'arraybuffer'
  | 'blob'
  | 'document'
  | 'json'
  | 'text'
  | 'stream'

export interface TransitionalOptions{
  silentJSONParsing: boolean;
  forcedJSONParsing: boolean;
  clarifyTimeoutError: boolean;
}

export interface AxiosRequestConfig {
  url?: string;
  method?: Method;
  baseURL?: string;
  transformRequest?: AxiosTransformer | AxiosTransformer[];
  transformResponse?: AxiosTransformer | AxiosTransformer[];
  headers?: any;
  params?: any;
  paramsSerializer?: (params: any) => string;
  data?: any;
  timeout?: number;
  timeoutErrorMessage?: string;
  withCredentials?: boolean;
  adapter?: AxiosAdapter;
  auth?: AxiosBasicCredentials;
  responseType?: ResponseType;
  xsrfCookieName?: string;
  xsrfHeaderName?: string;
  onUploadProgress?: (progressEvent: any) => void;
  onDownloadProgress?: (progressEvent: any) => void;
  maxContentLength?: number;
  validateStatus?: ((status: number) => boolean) | null;
  maxBodyLength?: number;
  maxRedirects?: number;
  socketPath?: string | null;
  httpAgent?: any;
  httpsAgent?: any;
  proxy?: AxiosProxyConfig | false;
  cancelToken?: CancelToken;
  decompress?: boolean;
  transitional?: TransitionalOptions
}

export interface AxiosResponse<T = any>  {
  data: T;
  status: number;
  statusText: string;
  headers: any;
  config: AxiosRequestConfig;
  request?: any;
}

export interface AxiosError<T = any> extends Error {
  config: AxiosRequestConfig;
  code?: string;
  request?: any;
  response?: AxiosResponse<T>;
  isAxiosError: boolean;
  toJSON: () => object;
}

export interface AxiosPromise<T = any> extends Promise<AxiosResponse<T>> {
}

export interface CancelStatic {
  new (message?: string): Cancel;
}

export interface Cancel {
  message: string;
}

export interface Canceler {
  (message?: string): void;
}

export interface CancelTokenStatic {
  new (executor: (cancel: Canceler) => void): CancelToken;
  source(): CancelTokenSource;
}

export interface CancelToken {
  promise: Promise<Cancel>;
  reason?: Cancel;
  throwIfRequested(): void;
}

export interface CancelTokenSource {
  token: CancelToken;
  cancel: Canceler;
}

export interface AxiosInterceptorManager<V> {
  use<T = V>(onFulfilled?: (value: V) => T | Promise<T>, onRejected?: (error: any) => any): number;
  eject(id: number): void;
}

export interface AxiosInstance {
  (config: AxiosRequestConfig): AxiosPromise;
  (url: string, config?: AxiosRequestConfig): AxiosPromise;
  defaults: AxiosRequestConfig;
  interceptors: {
    request: AxiosInterceptorManager<AxiosRequestConfig>;
    response: AxiosInterceptorManager<AxiosResponse>;
  };
  getUri(config?: AxiosRequestConfig): string;
  request<T = any, R = AxiosResponse<T>> (config: AxiosRequestConfig): Promise<R>;
  get<T = any, R = AxiosResponse<T>>(url: string, config?: AxiosRequestConfig): Promise<R>;
  delete<T = any, R = AxiosResponse<T>>(url: string, config?: AxiosRequestConfig): Promise<R>;
  head<T = any, R = AxiosResponse<T>>(url: string, config?: AxiosRequestConfig): Promise<R>;
  options<T = any, R = AxiosResponse<T>>(url: string, config?: AxiosRequestConfig): Promise<R>;
  post<T = any, R = AxiosResponse<T>>(url: string, data?: any, config?: AxiosRequestConfig): Promise<R>;
  put<T = any, R = AxiosResponse<T>>(url: string, data?: any, config?: AxiosRequestConfig): Promise<R>;
  patch<T = any, R = AxiosResponse<T>>(url: string, data?: any, config?: AxiosRequestConfig): Promise<R>;
}

export interface AxiosStatic extends AxiosInstance {
  create(config?: AxiosRequestConfig): AxiosInstance;
  Cancel: CancelStatic;
  CancelToken: CancelTokenStatic;
  isCancel(value: any): boolean;
  all<T>(values: (T | Promise<T>)[]): Promise<T[]>;
  spread<T, R>(callback: (...args: T[]) => R): (array: T[]) => R;
  isAxiosError(payload: any): payload is AxiosError;
}

declare const axios: AxiosStatic;

export default axios;

```

### node_modules\axios\index.js
```javascript
module.exports = require('./lib/axios');
```

### node_modules\axios\lib\adapters\README.md
```markdown
# axios // adapters

The modules under `adapters/` are modules that handle dispatching a request and settling a returned `Promise` once a response is received.

## Example

```js
var settle = require('./../core/settle');

module.exports = function myAdapter(config) {
  // At this point:
  //  - config has been merged with defaults
  //  - request transformers have already run
  //  - request interceptors have already run
  
  // Make the request using config provided
  // Upon response settle the Promise

  return new Promise(function(resolve, reject) {
  
    var response = {
      data: responseData,
      status: request.status,
      statusText: request.statusText,
      headers: responseHeaders,
      config: config,
      request: request
    };

    settle(resolve, reject, response);

    // From here:
    //  - response transformers will run
    //  - response interceptors will run
  });
}
```

```

### node_modules\axios\lib\adapters\http.js
```javascript
'use strict';

var utils = require('./../utils');
var settle = require('./../core/settle');
var buildFullPath = require('../core/buildFullPath');
var buildURL = require('./../helpers/buildURL');
var http = require('http');
var https = require('https');
var httpFollow = require('follow-redirects').http;
var httpsFollow = require('follow-redirects').https;
var url = require('url');
var zlib = require('zlib');
var pkg = require('./../../package.json');
var createError = require('../core/createError');
var enhanceError = require('../core/enhanceError');

var isHttps = /https:?/;

/**
 *
 * @param {http.ClientRequestArgs} options
 * @param {AxiosProxyConfig} proxy
 * @param {string} location
 */
function setProxy(options, proxy, location) {
  options.hostname = proxy.host;
  options.host = proxy.host;
  options.port = proxy.port;
  options.path = location;

  // Basic proxy authorization
  if (proxy.auth) {
    var base64 = Buffer.from(proxy.auth.username + ':' + proxy.auth.password, 'utf8').toString('base64');
    options.headers['Proxy-Authorization'] = 'Basic ' + base64;
  }

  // If a proxy is used, any redirects must also pass through the proxy
  options.beforeRedirect = function beforeRedirect(redirection) {
    redirection.headers.host = redirection.host;
    setProxy(redirection, proxy, redirection.href);
  };
}

/*eslint consistent-return:0*/
module.exports = function httpAdapter(config) {
  return new Promise(function dispatchHttpRequest(resolvePromise, rejectPromise) {
    var resolve = function resolve(value) {
      resolvePromise(value);
    };
    var reject = function reject(value) {
      rejectPromise(value);
    };
    var data = config.data;
    var headers = config.headers;

    // Set User-Agent (required by some servers)
    // See https://github.com/axios/axios/issues/69
    if ('User-Agent' in headers || 'user-agent' in headers) {
      // User-Agent is specified; handle case where no UA header is desired
      if (!headers['User-Agent'] && !headers['user-agent']) {
        delete headers['User-Agent'];
        delete headers['user-agent'];
      }
      // Otherwise, use specified value
    } else {
      // Only set header if it hasn't been set in config
      headers['User-Agent'] = 'axios/' + pkg.version;
    }

    if (data && !utils.isStream(data)) {
      if (Buffer.isBuffer(data)) {
        // Nothing to do...
      } else if (utils.isArrayBuffer(data)) {
        data = Buffer.from(new Uint8Array(data));
      } else if (utils.isString(data)) {
        data = Buffer.from(data, 'utf-8');
      } else {
        return reject(createError(
          'Data after transformation must be a string, an ArrayBuffer, a Buffer, or a Stream',
          config
        ));
      }

      // Add Content-Length header if data exists
      headers['Content-Length'] = data.length;
    }

    // HTTP basic authentication
    var auth = undefined;
    if (config.auth) {
      var username = config.auth.username || '';
      var password = config.auth.password || '';
      auth = username + ':' + password;
    }

    // Parse url
    var fullPath = buildFullPath(config.baseURL, config.url);
    var parsed = url.parse(fullPath);
    var protocol = parsed.protocol || 'http:';

    if (!auth && parsed.auth) {
      var urlAuth = parsed.auth.split(':');
      var urlUsername = urlAuth[0] || '';
      var urlPassword = urlAuth[1] || '';
      auth = urlUsername + ':' + urlPassword;
    }

    if (auth) {
      delete headers.Authorization;
    }

    var isHttpsRequest = isHttps.test(protocol);
    var agent = isHttpsRequest ? config.httpsAgent : config.httpAgent;

    var options = {
      path: buildURL(parsed.path, config.params, config.paramsSerializer).replace(/^\?/, ''),
      method: config.method.toUpperCase(),
      headers: headers,
      agent: agent,
      agents: { http: config.httpAgent, https: config.httpsAgent },
      auth: auth
    };

    if (config.socketPath) {
      options.socketPath = config.socketPath;
    } else {
      options.hostname = parsed.hostname;
      options.port = parsed.port;
    }

    var proxy = config.proxy;
    if (!proxy && proxy !== false) {
      var proxyEnv = protocol.slice(0, -1) + '_proxy';
      var proxyUrl = process.env[proxyEnv] || process.env[proxyEnv.toUpperCase()];
      if (proxyUrl) {
        var parsedProxyUrl = url.parse(proxyUrl);
        var noProxyEnv = process.env.no_proxy || process.env.NO_PROXY;
        var shouldProxy = true;

        if (noProxyEnv) {
          var noProxy = noProxyEnv.split(',').map(function trim(s) {
            return s.trim();
          });

          shouldProxy = !noProxy.some(function proxyMatch(proxyElement) {
            if (!proxyElement) {
              return false;
            }
            if (proxyElement === '*') {
              return true;
            }
            if (proxyElement[0] === '.' &&
                parsed.hostname.substr(parsed.hostname.length - proxyElement.length) === proxyElement) {
              return true;
            }

            return parsed.hostname === proxyElement;
          });
        }

        if (shouldProxy) {
          proxy = {
            host: parsedProxyUrl.hostname,
            port: parsedProxyUrl.port,
            protocol: parsedProxyUrl.protocol
          };

          if (parsedProxyUrl.auth) {
            var proxyUrlAuth = parsedProxyUrl.auth.split(':');
            proxy.auth = {
              username: proxyUrlAuth[0],
              password: proxyUrlAuth[1]
            };
          }
        }
      }
    }

    if (proxy) {
      options.headers.host = parsed.hostname + (parsed.port ? ':' + parsed.port : '');
      setProxy(options, proxy, protocol + '//' + parsed.hostname + (parsed.port ? ':' + parsed.port : '') + options.path);
    }

    var transport;
    var isHttpsProxy = isHttpsRequest && (proxy ? isHttps.test(proxy.protocol) : true);
    if (config.transport) {
      transport = config.transport;
    } else if (config.maxRedirects === 0) {
      transport = isHttpsProxy ? https : http;
    } else {
      if (config.maxRedirects) {
        options.maxRedirects = config.maxRedirects;
      }
      transport = isHttpsProxy ? httpsFollow : httpFollow;
    }

    if (config.maxBodyLength > -1) {
      options.maxBodyLength = config.maxBodyLength;
    }

    // Create the request
    var req = transport.request(options, function handleResponse(res) {
      if (req.aborted) return;

      // uncompress the response body transparently if required
      var stream = res;

      // return the last request in case of redirects
      var lastRequest = res.req || req;


      // if no content, is HEAD request or decompress disabled we should not decompress
      if (res.statusCode !== 204 && lastRequest.method !== 'HEAD' && config.decompress !== false) {
        switch (res.headers['content-encoding']) {
        /*eslint default-case:0*/
        case 'gzip':
        case 'compress':
        case 'deflate':
        // add the unzipper to the body stream processing pipeline
          stream = stream.pipe(zlib.createUnzip());

          // remove the content-encoding in order to not confuse downstream operations
          delete res.headers['content-encoding'];
          break;
        }
      }

      var response = {
        status: res.statusCode,
        statusText: res.statusMessage,
        headers: res.headers,
        config: config,
        request: lastRequest
      };

      if (config.responseType === 'stream') {
        response.data = stream;
        settle(resolve, reject, response);
      } else {
        var responseBuffer = [];
        var totalResponseBytes = 0;
        stream.on('data', function handleStreamData(chunk) {
          responseBuffer.push(chunk);
          totalResponseBytes += chunk.length;

          // make sure the content length is not over the maxContentLength if specified
          if (config.maxContentLength > -1 && totalResponseBytes > config.maxContentLength) {
            stream.destroy();
            reject(createError('maxContentLength size of ' + config.maxContentLength + ' exceeded',
              config, null, lastRequest));
          }
        });

        stream.on('error', function handleStreamError(err) {
          if (req.aborted) return;
          reject(enhanceError(err, config, null, lastRequest));
        });

        stream.on('end', function handleStreamEnd() {
          var responseData = Buffer.concat(responseBuffer);
          if (config.responseType !== 'arraybuffer') {
            responseData = responseData.toString(config.responseEncoding);
            if (!config.responseEncoding || config.responseEncoding === 'utf8') {
              responseData = utils.stripBOM(responseData);
            }
          }

          response.data = responseData;
          settle(resolve, reject, response);
        });
      }
    });

    // Handle errors
    req.on('error', function handleRequestError(err) {
      if (req.aborted && err.code !== 'ERR_FR_TOO_MANY_REDIRECTS') return;
      reject(enhanceError(err, config, null, req));
    });

    // Handle request timeout
    if (config.timeout) {
      // This is forcing a int timeout to avoid problems if the `req` interface doesn't handle other types.
      var timeout = parseInt(config.timeout, 10);

      if (isNaN(timeout)) {
        reject(createError(
          'error trying to parse `config.timeout` to int',
          config,
          'ERR_PARSE_TIMEOUT',
          req
        ));

        return;
      }

      // Sometime, the response will be very slow, and does not respond, the connect event will be block by event loop system.
      // And timer callback will be fired, and abort() will be invoked before connection, then get "socket hang up" and code ECONNRESET.
      // At this time, if we have a large number of request, nodejs will hang up some socket on background. and the number will up and up.
      // And then these socket which be hang up will devoring CPU little by little.
      // ClientRequest.setTimeout will be fired on the specify milliseconds, and can make sure that abort() will be fired after connect.
      req.setTimeout(timeout, function handleRequestTimeout() {
        req.abort();
        reject(createError(
          'timeout of ' + timeout + 'ms exceeded',
          config,
          config.transitional && config.transitional.clarifyTimeoutError ? 'ETIMEDOUT' : 'ECONNABORTED',
          req
        ));
      });
    }

    if (config.cancelToken) {
      // Handle cancellation
      config.cancelToken.promise.then(function onCanceled(cancel) {
        if (req.aborted) return;

        req.abort();
        reject(cancel);
      });
    }

    // Send the request
    if (utils.isStream(data)) {
      data.on('error', function handleStreamError(err) {
        reject(enhanceError(err, config, null, req));
      }).pipe(req);
    } else {
      req.end(data);
    }
  });
};

```

### node_modules\axios\lib\adapters\xhr.js
```javascript
'use strict';

var utils = require('./../utils');
var settle = require('./../core/settle');
var cookies = require('./../helpers/cookies');
var buildURL = require('./../helpers/buildURL');
var buildFullPath = require('../core/buildFullPath');
var parseHeaders = require('./../helpers/parseHeaders');
var isURLSameOrigin = require('./../helpers/isURLSameOrigin');
var createError = require('../core/createError');

module.exports = function xhrAdapter(config) {
  return new Promise(function dispatchXhrRequest(resolve, reject) {
    var requestData = config.data;
    var requestHeaders = config.headers;
    var responseType = config.responseType;

    if (utils.isFormData(requestData)) {
      delete requestHeaders['Content-Type']; // Let the browser set it
    }

    var request = new XMLHttpRequest();

    // HTTP basic authentication
    if (config.auth) {
      var username = config.auth.username || '';
      var password = config.auth.password ? unescape(encodeURIComponent(config.auth.password)) : '';
      requestHeaders.Authorization = 'Basic ' + btoa(username + ':' + password);
    }

    var fullPath = buildFullPath(config.baseURL, config.url);
    request.open(config.method.toUpperCase(), buildURL(fullPath, config.params, config.paramsSerializer), true);

    // Set the request timeout in MS
    request.timeout = config.timeout;

    function onloadend() {
      if (!request) {
        return;
      }
      // Prepare the response
      var responseHeaders = 'getAllResponseHeaders' in request ? parseHeaders(request.getAllResponseHeaders()) : null;
      var responseData = !responseType || responseType === 'text' ||  responseType === 'json' ?
        request.responseText : request.response;
      var response = {
        data: responseData,
        status: request.status,
        statusText: request.statusText,
        headers: responseHeaders,
        config: config,
        request: request
      };

      settle(resolve, reject, response);

      // Clean up request
      request = null;
    }

    if ('onloadend' in request) {
      // Use onloadend if available
      request.onloadend = onloadend;
    } else {
      // Listen for ready state to emulate onloadend
      request.onreadystatechange = function handleLoad() {
        if (!request || request.readyState !== 4) {
          return;
        }

        // The request errored out and we didn't get a response, this will be
        // handled by onerror instead
        // With one exception: request that using file: protocol, most browsers
        // will return status as 0 even though it's a successful request
        if (request.status === 0 && !(request.responseURL && request.responseURL.indexOf('file:') === 0)) {
          return;
        }
        // readystate handler is calling before onerror or ontimeout handlers,
        // so we should call onloadend on the next 'tick'
        setTimeout(onloadend);
      };
    }

    // Handle browser request cancellation (as opposed to a manual cancellation)
    request.onabort = function handleAbort() {
      if (!request) {
        return;
      }

      reject(createError('Request aborted', config, 'ECONNABORTED', request));

      // Clean up request
      request = null;
    };

    // Handle low level network errors
    request.onerror = function handleError() {
      // Real errors are hidden from us by the browser
      // onerror should only fire if it's a network error
      reject(createError('Network Error', config, null, request));

      // Clean up request
      request = null;
    };

    // Handle timeout
    request.ontimeout = function handleTimeout() {
      var timeoutErrorMessage = 'timeout of ' + config.timeout + 'ms exceeded';
      if (config.timeoutErrorMessage) {
        timeoutErrorMessage = config.timeoutErrorMessage;
      }
      reject(createError(
        timeoutErrorMessage,
        config,
        config.transitional && config.transitional.clarifyTimeoutError ? 'ETIMEDOUT' : 'ECONNABORTED',
        request));

      // Clean up request
      request = null;
    };

    // Add xsrf header
    // This is only done if running in a standard browser environment.
    // Specifically not if we're in a web worker, or react-native.
    if (utils.isStandardBrowserEnv()) {
      // Add xsrf header
      var xsrfValue = (config.withCredentials || isURLSameOrigin(fullPath)) && config.xsrfCookieName ?
        cookies.read(config.xsrfCookieName) :
        undefined;

      if (xsrfValue) {
        requestHeaders[config.xsrfHeaderName] = xsrfValue;
      }
    }

    // Add headers to the request
    if ('setRequestHeader' in request) {
      utils.forEach(requestHeaders, function setRequestHeader(val, key) {
        if (typeof requestData === 'undefined' && key.toLowerCase() === 'content-type') {
          // Remove Content-Type if data is undefined
          delete requestHeaders[key];
        } else {
          // Otherwise add header to the request
          request.setRequestHeader(key, val);
        }
      });
    }

    // Add withCredentials to request if needed
    if (!utils.isUndefined(config.withCredentials)) {
      request.withCredentials = !!config.withCredentials;
    }

    // Add responseType to request if needed
    if (responseType && responseType !== 'json') {
      request.responseType = config.responseType;
    }

    // Handle progress if needed
    if (typeof config.onDownloadProgress === 'function') {
      request.addEventListener('progress', config.onDownloadProgress);
    }

    // Not all browsers support upload events
    if (typeof config.onUploadProgress === 'function' && request.upload) {
      request.upload.addEventListener('progress', config.onUploadProgress);
    }

    if (config.cancelToken) {
      // Handle cancellation
      config.cancelToken.promise.then(function onCanceled(cancel) {
        if (!request) {
          return;
        }

        request.abort();
        reject(cancel);
        // Clean up request
        request = null;
      });
    }

    if (!requestData) {
      requestData = null;
    }

    // Send the request
    request.send(requestData);
  });
};

```

### node_modules\axios\lib\axios.js
```javascript
'use strict';

var utils = require('./utils');
var bind = require('./helpers/bind');
var Axios = require('./core/Axios');
var mergeConfig = require('./core/mergeConfig');
var defaults = require('./defaults');

/**
 * Create an instance of Axios
 *
 * @param {Object} defaultConfig The default config for the instance
 * @return {Axios} A new instance of Axios
 */
function createInstance(defaultConfig) {
  var context = new Axios(defaultConfig);
  var instance = bind(Axios.prototype.request, context);

  // Copy axios.prototype to instance
  utils.extend(instance, Axios.prototype, context);

  // Copy context to instance
  utils.extend(instance, context);

  return instance;
}

// Create the default instance to be exported
var axios = createInstance(defaults);

// Expose Axios class to allow class inheritance
axios.Axios = Axios;

// Factory for creating new instances
axios.create = function create(instanceConfig) {
  return createInstance(mergeConfig(axios.defaults, instanceConfig));
};

// Expose Cancel & CancelToken
axios.Cancel = require('./cancel/Cancel');
axios.CancelToken = require('./cancel/CancelToken');
axios.isCancel = require('./cancel/isCancel');

// Expose all/spread
axios.all = function all(promises) {
  return Promise.all(promises);
};
axios.spread = require('./helpers/spread');

// Expose isAxiosError
axios.isAxiosError = require('./helpers/isAxiosError');

module.exports = axios;

// Allow use of default import syntax in TypeScript
module.exports.default = axios;

```

### node_modules\axios\lib\cancel\Cancel.js
```javascript
'use strict';

/**
 * A `Cancel` is an object that is thrown when an operation is canceled.
 *
 * @class
 * @param {string=} message The message.
 */
function Cancel(message) {
  this.message = message;
}

Cancel.prototype.toString = function toString() {
  return 'Cancel' + (this.message ? ': ' + this.message : '');
};

Cancel.prototype.__CANCEL__ = true;

module.exports = Cancel;

```

### node_modules\axios\lib\cancel\CancelToken.js
```javascript
'use strict';

var Cancel = require('./Cancel');

/**
 * A `CancelToken` is an object that can be used to request cancellation of an operation.
 *
 * @class
 * @param {Function} executor The executor function.
 */
function CancelToken(executor) {
  if (typeof executor !== 'function') {
    throw new TypeError('executor must be a function.');
  }

  var resolvePromise;
  this.promise = new Promise(function promiseExecutor(resolve) {
    resolvePromise = resolve;
  });

  var token = this;
  executor(function cancel(message) {
    if (token.reason) {
      // Cancellation has already been requested
      return;
    }

    token.reason = new Cancel(message);
    resolvePromise(token.reason);
  });
}

/**
 * Throws a `Cancel` if cancellation has been requested.
 */
CancelToken.prototype.throwIfRequested = function throwIfRequested() {
  if (this.reason) {
    throw this.reason;
  }
};

/**
 * Returns an object that contains a new `CancelToken` and a function that, when called,
 * cancels the `CancelToken`.
 */
CancelToken.source = function source() {
  var cancel;
  var token = new CancelToken(function executor(c) {
    cancel = c;
  });
  return {
    token: token,
    cancel: cancel
  };
};

module.exports = CancelToken;

```

### node_modules\axios\lib\cancel\isCancel.js
```javascript
'use strict';

module.exports = function isCancel(value) {
  return !!(value && value.__CANCEL__);
};

```

### node_modules\axios\lib\core\Axios.js
```javascript
'use strict';

var utils = require('./../utils');
var buildURL = require('../helpers/buildURL');
var InterceptorManager = require('./InterceptorManager');
var dispatchRequest = require('./dispatchRequest');
var mergeConfig = require('./mergeConfig');
var validator = require('../helpers/validator');

var validators = validator.validators;
/**
 * Create a new instance of Axios
 *
 * @param {Object} instanceConfig The default config for the instance
 */
function Axios(instanceConfig) {
  this.defaults = instanceConfig;
  this.interceptors = {
    request: new InterceptorManager(),
    response: new InterceptorManager()
  };
}

/**
 * Dispatch a request
 *
 * @param {Object} config The config specific for this request (merged with this.defaults)
 */
Axios.prototype.request = function request(config) {
  /*eslint no-param-reassign:0*/
  // Allow for axios('example/url'[, config]) a la fetch API
  if (typeof config === 'string') {
    config = arguments[1] || {};
    config.url = arguments[0];
  } else {
    config = config || {};
  }

  config = mergeConfig(this.defaults, config);

  // Set config.method
  if (config.method) {
    config.method = config.method.toLowerCase();
  } else if (this.defaults.method) {
    config.method = this.defaults.method.toLowerCase();
  } else {
    config.method = 'get';
  }

  var transitional = config.transitional;

  if (transitional !== undefined) {
    validator.assertOptions(transitional, {
      silentJSONParsing: validators.transitional(validators.boolean, '1.0.0'),
      forcedJSONParsing: validators.transitional(validators.boolean, '1.0.0'),
      clarifyTimeoutError: validators.transitional(validators.boolean, '1.0.0')
    }, false);
  }

  // filter out skipped interceptors
  var requestInterceptorChain = [];
  var synchronousRequestInterceptors = true;
  this.interceptors.request.forEach(function unshiftRequestInterceptors(interceptor) {
    if (typeof interceptor.runWhen === 'function' && interceptor.runWhen(config) === false) {
      return;
    }

    synchronousRequestInterceptors = synchronousRequestInterceptors && interceptor.synchronous;

    requestInterceptorChain.unshift(interceptor.fulfilled, interceptor.rejected);
  });

  var responseInterceptorChain = [];
  this.interceptors.response.forEach(function pushResponseInterceptors(interceptor) {
    responseInterceptorChain.push(interceptor.fulfilled, interceptor.rejected);
  });

  var promise;

  if (!synchronousRequestInterceptors) {
    var chain = [dispatchRequest, undefined];

    Array.prototype.unshift.apply(chain, requestInterceptorChain);
    chain = chain.concat(responseInterceptorChain);

    promise = Promise.resolve(config);
    while (chain.length) {
      promise = promise.then(chain.shift(), chain.shift());
    }

    return promise;
  }


  var newConfig = config;
  while (requestInterceptorChain.length) {
    var onFulfilled = requestInterceptorChain.shift();
    var onRejected = requestInterceptorChain.shift();
    try {
      newConfig = onFulfilled(newConfig);
    } catch (error) {
      onRejected(error);
      break;
    }
  }

  try {
    promise = dispatchRequest(newConfig);
  } catch (error) {
    return Promise.reject(error);
  }

  while (responseInterceptorChain.length) {
    promise = promise.then(responseInterceptorChain.shift(), responseInterceptorChain.shift());
  }

  return promise;
};

Axios.prototype.getUri = function getUri(config) {
  config = mergeConfig(this.defaults, config);
  return buildURL(config.url, config.params, config.paramsSerializer).replace(/^\?/, '');
};

// Provide aliases for supported request methods
utils.forEach(['delete', 'get', 'head', 'options'], function forEachMethodNoData(method) {
  /*eslint func-names:0*/
  Axios.prototype[method] = function(url, config) {
    return this.request(mergeConfig(config || {}, {
      method: method,
      url: url,
      data: (config || {}).data
    }));
  };
});

utils.forEach(['post', 'put', 'patch'], function forEachMethodWithData(method) {
  /*eslint func-names:0*/
  Axios.prototype[method] = function(url, data, config) {
    return this.request(mergeConfig(config || {}, {
      method: method,
      url: url,
      data: data
    }));
  };
});

module.exports = Axios;

```

### node_modules\axios\lib\core\InterceptorManager.js
```javascript
'use strict';

var utils = require('./../utils');

function InterceptorManager() {
  this.handlers = [];
}

/**
 * Add a new interceptor to the stack
 *
 * @param {Function} fulfilled The function to handle `then` for a `Promise`
 * @param {Function} rejected The function to handle `reject` for a `Promise`
 *
 * @return {Number} An ID used to remove interceptor later
 */
InterceptorManager.prototype.use = function use(fulfilled, rejected, options) {
  this.handlers.push({
    fulfilled: fulfilled,
    rejected: rejected,
    synchronous: options ? options.synchronous : false,
    runWhen: options ? options.runWhen : null
  });
  return this.handlers.length - 1;
};

/**
 * Remove an interceptor from the stack
 *
 * @param {Number} id The ID that was returned by `use`
 */
InterceptorManager.prototype.eject = function eject(id) {
  if (this.handlers[id]) {
    this.handlers[id] = null;
  }
};

/**
 * Iterate over all the registered interceptors
 *
 * This method is particularly useful for skipping over any
 * interceptors that may have become `null` calling `eject`.
 *
 * @param {Function} fn The function to call for each interceptor
 */
InterceptorManager.prototype.forEach = function forEach(fn) {
  utils.forEach(this.handlers, function forEachHandler(h) {
    if (h !== null) {
      fn(h);
    }
  });
};

module.exports = InterceptorManager;

```

### node_modules\axios\lib\core\README.md
```markdown
# axios // core

The modules found in `core/` should be modules that are specific to the domain logic of axios. These modules would most likely not make sense to be consumed outside of the axios module, as their logic is too specific. Some examples of core modules are:

- Dispatching requests
  - Requests sent via `adapters/` (see lib/adapters/README.md)
- Managing interceptors
- Handling config

```

### node_modules\axios\lib\core\buildFullPath.js
```javascript
'use strict';

var isAbsoluteURL = require('../helpers/isAbsoluteURL');
var combineURLs = require('../helpers/combineURLs');

/**
 * Creates a new URL by combining the baseURL with the requestedURL,
 * only when the requestedURL is not already an absolute URL.
 * If the requestURL is absolute, this function returns the requestedURL untouched.
 *
 * @param {string} baseURL The base URL
 * @param {string} requestedURL Absolute or relative URL to combine
 * @returns {string} The combined full path
 */
module.exports = function buildFullPath(baseURL, requestedURL) {
  if (baseURL && !isAbsoluteURL(requestedURL)) {
    return combineURLs(baseURL, requestedURL);
  }
  return requestedURL;
};

```

### node_modules\axios\lib\core\createError.js
```javascript
'use strict';

var enhanceError = require('./enhanceError');

/**
 * Create an Error with the specified message, config, error code, request and response.
 *
 * @param {string} message The error message.
 * @param {Object} config The config.
 * @param {string} [code] The error code (for example, 'ECONNABORTED').
 * @param {Object} [request] The request.
 * @param {Object} [response] The response.
 * @returns {Error} The created error.
 */
module.exports = function createError(message, config, code, request, response) {
  var error = new Error(message);
  return enhanceError(error, config, code, request, response);
};

```

### node_modules\axios\lib\core\dispatchRequest.js
```javascript
'use strict';

var utils = require('./../utils');
var transformData = require('./transformData');
var isCancel = require('../cancel/isCancel');
var defaults = require('../defaults');

/**
 * Throws a `Cancel` if cancellation has been requested.
 */
function throwIfCancellationRequested(config) {
  if (config.cancelToken) {
    config.cancelToken.throwIfRequested();
  }
}

/**
 * Dispatch a request to the server using the configured adapter.
 *
 * @param {object} config The config that is to be used for the request
 * @returns {Promise} The Promise to be fulfilled
 */
module.exports = function dispatchRequest(config) {
  throwIfCancellationRequested(config);

  // Ensure headers exist
  config.headers = config.headers || {};

  // Transform request data
  config.data = transformData.call(
    config,
    config.data,
    config.headers,
    config.transformRequest
  );

  // Flatten headers
  config.headers = utils.merge(
    config.headers.common || {},
    config.headers[config.method] || {},
    config.headers
  );

  utils.forEach(
    ['delete', 'get', 'head', 'post', 'put', 'patch', 'common'],
    function cleanHeaderConfig(method) {
      delete config.headers[method];
    }
  );

  var adapter = config.adapter || defaults.adapter;

  return adapter(config).then(function onAdapterResolution(response) {
    throwIfCancellationRequested(config);

    // Transform response data
    response.data = transformData.call(
      config,
      response.data,
      response.headers,
      config.transformResponse
    );

    return response;
  }, function onAdapterRejection(reason) {
    if (!isCancel(reason)) {
      throwIfCancellationRequested(config);

      // Transform response data
      if (reason && reason.response) {
        reason.response.data = transformData.call(
          config,
          reason.response.data,
          reason.response.headers,
          config.transformResponse
        );
      }
    }

    return Promise.reject(reason);
  });
};

```

### node_modules\axios\lib\core\enhanceError.js
```javascript
'use strict';

/**
 * Update an Error with the specified config, error code, and response.
 *
 * @param {Error} error The error to update.
 * @param {Object} config The config.
 * @param {string} [code] The error code (for example, 'ECONNABORTED').
 * @param {Object} [request] The request.
 * @param {Object} [response] The response.
 * @returns {Error} The error.
 */
module.exports = function enhanceError(error, config, code, request, response) {
  error.config = config;
  if (code) {
    error.code = code;
  }

  error.request = request;
  error.response = response;
  error.isAxiosError = true;

  error.toJSON = function toJSON() {
    return {
      // Standard
      message: this.message,
      name: this.name,
      // Microsoft
      description: this.description,
      number: this.number,
      // Mozilla
      fileName: this.fileName,
      lineNumber: this.lineNumber,
      columnNumber: this.columnNumber,
      stack: this.stack,
      // Axios
      config: this.config,
      code: this.code
    };
  };
  return error;
};

```

### node_modules\axios\lib\core\mergeConfig.js
```javascript
'use strict';

var utils = require('../utils');

/**
 * Config-specific merge-function which creates a new config-object
 * by merging two configuration objects together.
 *
 * @param {Object} config1
 * @param {Object} config2
 * @returns {Object} New object resulting from merging config2 to config1
 */
module.exports = function mergeConfig(config1, config2) {
  // eslint-disable-next-line no-param-reassign
  config2 = config2 || {};
  var config = {};

  var valueFromConfig2Keys = ['url', 'method', 'data'];
  var mergeDeepPropertiesKeys = ['headers', 'auth', 'proxy', 'params'];
  var defaultToConfig2Keys = [
    'baseURL', 'transformRequest', 'transformResponse', 'paramsSerializer',
    'timeout', 'timeoutMessage', 'withCredentials', 'adapter', 'responseType', 'xsrfCookieName',
    'xsrfHeaderName', 'onUploadProgress', 'onDownloadProgress', 'decompress',
    'maxContentLength', 'maxBodyLength', 'maxRedirects', 'transport', 'httpAgent',
    'httpsAgent', 'cancelToken', 'socketPath', 'responseEncoding'
  ];
  var directMergeKeys = ['validateStatus'];

  function getMergedValue(target, source) {
    if (utils.isPlainObject(target) && utils.isPlainObject(source)) {
      return utils.merge(target, source);
    } else if (utils.isPlainObject(source)) {
      return utils.merge({}, source);
    } else if (utils.isArray(source)) {
      return source.slice();
    }
    return source;
  }

  function mergeDeepProperties(prop) {
    if (!utils.isUndefined(config2[prop])) {
      config[prop] = getMergedValue(config1[prop], config2[prop]);
    } else if (!utils.isUndefined(config1[prop])) {
      config[prop] = getMergedValue(undefined, config1[prop]);
    }
  }

  utils.forEach(valueFromConfig2Keys, function valueFromConfig2(prop) {
    if (!utils.isUndefined(config2[prop])) {
      config[prop] = getMergedValue(undefined, config2[prop]);
    }
  });

  utils.forEach(mergeDeepPropertiesKeys, mergeDeepProperties);

  utils.forEach(defaultToConfig2Keys, function defaultToConfig2(prop) {
    if (!utils.isUndefined(config2[prop])) {
      config[prop] = getMergedValue(undefined, config2[prop]);
    } else if (!utils.isUndefined(config1[prop])) {
      config[prop] = getMergedValue(undefined, config1[prop]);
    }
  });

  utils.forEach(directMergeKeys, function merge(prop) {
    if (prop in config2) {
      config[prop] = getMergedValue(config1[prop], config2[prop]);
    } else if (prop in config1) {
      config[prop] = getMergedValue(undefined, config1[prop]);
    }
  });

  var axiosKeys = valueFromConfig2Keys
    .concat(mergeDeepPropertiesKeys)
    .concat(defaultToConfig2Keys)
    .concat(directMergeKeys);

  var otherKeys = Object
    .keys(config1)
    .concat(Object.keys(config2))
    .filter(function filterAxiosKeys(key) {
      return axiosKeys.indexOf(key) === -1;
    });

  utils.forEach(otherKeys, mergeDeepProperties);

  return config;
};

```

### node_modules\axios\lib\core\settle.js
```javascript
'use strict';

var createError = require('./createError');

/**
 * Resolve or reject a Promise based on response status.
 *
 * @param {Function} resolve A function that resolves the promise.
 * @param {Function} reject A function that rejects the promise.
 * @param {object} response The response.
 */
module.exports = function settle(resolve, reject, response) {
  var validateStatus = response.config.validateStatus;
  if (!response.status || !validateStatus || validateStatus(response.status)) {
    resolve(response);
  } else {
    reject(createError(
      'Request failed with status code ' + response.status,
      response.config,
      null,
      response.request,
      response
    ));
  }
};

```

### node_modules\axios\lib\core\transformData.js
```javascript
'use strict';

var utils = require('./../utils');
var defaults = require('./../defaults');

/**
 * Transform the data for a request or a response
 *
 * @param {Object|String} data The data to be transformed
 * @param {Array} headers The headers for the request or response
 * @param {Array|Function} fns A single function or Array of functions
 * @returns {*} The resulting transformed data
 */
module.exports = function transformData(data, headers, fns) {
  var context = this || defaults;
  /*eslint no-param-reassign:0*/
  utils.forEach(fns, function transform(fn) {
    data = fn.call(context, data, headers);
  });

  return data;
};

```

### node_modules\axios\lib\defaults.js
```javascript
'use strict';

var utils = require('./utils');
var normalizeHeaderName = require('./helpers/normalizeHeaderName');
var enhanceError = require('./core/enhanceError');

var DEFAULT_CONTENT_TYPE = {
  'Content-Type': 'application/x-www-form-urlencoded'
};

function setContentTypeIfUnset(headers, value) {
  if (!utils.isUndefined(headers) && utils.isUndefined(headers['Content-Type'])) {
    headers['Content-Type'] = value;
  }
}

function getDefaultAdapter() {
  var adapter;
  if (typeof XMLHttpRequest !== 'undefined') {
    // For browsers use XHR adapter
    adapter = require('./adapters/xhr');
  } else if (typeof process !== 'undefined' && Object.prototype.toString.call(process) === '[object process]') {
    // For node use HTTP adapter
    adapter = require('./adapters/http');
  }
  return adapter;
}

function stringifySafely(rawValue, parser, encoder) {
  if (utils.isString(rawValue)) {
    try {
      (parser || JSON.parse)(rawValue);
      return utils.trim(rawValue);
    } catch (e) {
      if (e.name !== 'SyntaxError') {
        throw e;
      }
    }
  }

  return (encoder || JSON.stringify)(rawValue);
}

var defaults = {

  transitional: {
    silentJSONParsing: true,
    forcedJSONParsing: true,
    clarifyTimeoutError: false
  },

  adapter: getDefaultAdapter(),

  transformRequest: [function transformRequest(data, headers) {
    normalizeHeaderName(headers, 'Accept');
    normalizeHeaderName(headers, 'Content-Type');

    if (utils.isFormData(data) ||
      utils.isArrayBuffer(data) ||
      utils.isBuffer(data) ||
      utils.isStream(data) ||
      utils.isFile(data) ||
      utils.isBlob(data)
    ) {
      return data;
    }
    if (utils.isArrayBufferView(data)) {
      return data.buffer;
    }
    if (utils.isURLSearchParams(data)) {
      setContentTypeIfUnset(headers, 'application/x-www-form-urlencoded;charset=utf-8');
      return data.toString();
    }
    if (utils.isObject(data) || (headers && headers['Content-Type'] === 'application/json')) {
      setContentTypeIfUnset(headers, 'application/json');
      return stringifySafely(data);
    }
    return data;
  }],

  transformResponse: [function transformResponse(data) {
    var transitional = this.transitional;
    var silentJSONParsing = transitional && transitional.silentJSONParsing;
    var forcedJSONParsing = transitional && transitional.forcedJSONParsing;
    var strictJSONParsing = !silentJSONParsing && this.responseType === 'json';

    if (strictJSONParsing || (forcedJSONParsing && utils.isString(data) && data.length)) {
      try {
        return JSON.parse(data);
      } catch (e) {
        if (strictJSONParsing) {
          if (e.name === 'SyntaxError') {
            throw enhanceError(e, this, 'E_JSON_PARSE');
          }
          throw e;
        }
      }
    }

    return data;
  }],

  /**
   * A timeout in milliseconds to abort a request. If set to 0 (default) a
   * timeout is not created.
   */
  timeout: 0,

  xsrfCookieName: 'XSRF-TOKEN',
  xsrfHeaderName: 'X-XSRF-TOKEN',

  maxContentLength: -1,
  maxBodyLength: -1,

  validateStatus: function validateStatus(status) {
    return status >= 200 && status < 300;
  }
};

defaults.headers = {
  common: {
    'Accept': 'application/json, text/plain, */*'
  }
};

utils.forEach(['delete', 'get', 'head'], function forEachMethodNoData(method) {
  defaults.headers[method] = {};
});

utils.forEach(['post', 'put', 'patch'], function forEachMethodWithData(method) {
  defaults.headers[method] = utils.merge(DEFAULT_CONTENT_TYPE);
});

module.exports = defaults;

```

### node_modules\axios\lib\helpers\README.md
```markdown
# axios // helpers

The modules found in `helpers/` should be generic modules that are _not_ specific to the domain logic of axios. These modules could theoretically be published to npm on their own and consumed by other modules or apps. Some examples of generic modules are things like:

- Browser polyfills
- Managing cookies
- Parsing HTTP headers

```

### node_modules\axios\lib\helpers\bind.js
```javascript
'use strict';

module.exports = function bind(fn, thisArg) {
  return function wrap() {
    var args = new Array(arguments.length);
    for (var i = 0; i < args.length; i++) {
      args[i] = arguments[i];
    }
    return fn.apply(thisArg, args);
  };
};

```

### node_modules\axios\lib\helpers\buildURL.js
```javascript
'use strict';

var utils = require('./../utils');

function encode(val) {
  return encodeURIComponent(val).
    replace(/%3A/gi, ':').
    replace(/%24/g, '$').
    replace(/%2C/gi, ',').
    replace(/%20/g, '+').
    replace(/%5B/gi, '[').
    replace(/%5D/gi, ']');
}

/**
 * Build a URL by appending params to the end
 *
 * @param {string} url The base of the url (e.g., http://www.google.com)
 * @param {object} [params] The params to be appended
 * @returns {string} The formatted url
 */
module.exports = function buildURL(url, params, paramsSerializer) {
  /*eslint no-param-reassign:0*/
  if (!params) {
    return url;
  }

  var serializedParams;
  if (paramsSerializer) {
    serializedParams = paramsSerializer(params);
  } else if (utils.isURLSearchParams(params)) {
    serializedParams = params.toString();
  } else {
    var parts = [];

    utils.forEach(params, function serialize(val, key) {
      if (val === null || typeof val === 'undefined') {
        return;
      }

      if (utils.isArray(val)) {
        key = key + '[]';
      } else {
        val = [val];
      }

      utils.forEach(val, function parseValue(v) {
        if (utils.isDate(v)) {
          v = v.toISOString();
        } else if (utils.isObject(v)) {
          v = JSON.stringify(v);
        }
        parts.push(encode(key) + '=' + encode(v));
      });
    });

    serializedParams = parts.join('&');
  }

  if (serializedParams) {
    var hashmarkIndex = url.indexOf('#');
    if (hashmarkIndex !== -1) {
      url = url.slice(0, hashmarkIndex);
    }

    url += (url.indexOf('?') === -1 ? '?' : '&') + serializedParams;
  }

  return url;
};

```

### node_modules\axios\lib\helpers\combineURLs.js
```javascript
'use strict';

/**
 * Creates a new URL by combining the specified URLs
 *
 * @param {string} baseURL The base URL
 * @param {string} relativeURL The relative URL
 * @returns {string} The combined URL
 */
module.exports = function combineURLs(baseURL, relativeURL) {
  return relativeURL
    ? baseURL.replace(/\/+$/, '') + '/' + relativeURL.replace(/^\/+/, '')
    : baseURL;
};

```

### node_modules\axios\lib\helpers\cookies.js
```javascript
'use strict';

var utils = require('./../utils');

module.exports = (
  utils.isStandardBrowserEnv() ?

  // Standard browser envs support document.cookie
    (function standardBrowserEnv() {
      return {
        write: function write(name, value, expires, path, domain, secure) {
          var cookie = [];
          cookie.push(name + '=' + encodeURIComponent(value));

          if (utils.isNumber(expires)) {
            cookie.push('expires=' + new Date(expires).toGMTString());
          }

          if (utils.isString(path)) {
            cookie.push('path=' + path);
          }

          if (utils.isString(domain)) {
            cookie.push('domain=' + domain);
          }

          if (secure === true) {
            cookie.push('secure');
          }

          document.cookie = cookie.join('; ');
        },

        read: function read(name) {
          var match = document.cookie.match(new RegExp('(^|;\\s*)(' + name + ')=([^;]*)'));
          return (match ? decodeURIComponent(match[3]) : null);
        },

        remove: function remove(name) {
          this.write(name, '', Date.now() - 86400000);
        }
      };
    })() :

  // Non standard browser env (web workers, react-native) lack needed support.
    (function nonStandardBrowserEnv() {
      return {
        write: function write() {},
        read: function read() { return null; },
        remove: function remove() {}
      };
    })()
);

```

### node_modules\axios\lib\helpers\deprecatedMethod.js
```javascript
'use strict';

/*eslint no-console:0*/

/**
 * Supply a warning to the developer that a method they are using
 * has been deprecated.
 *
 * @param {string} method The name of the deprecated method
 * @param {string} [instead] The alternate method to use if applicable
 * @param {string} [docs] The documentation URL to get further details
 */
module.exports = function deprecatedMethod(method, instead, docs) {
  try {
    console.warn(
      'DEPRECATED method `' + method + '`.' +
      (instead ? ' Use `' + instead + '` instead.' : '') +
      ' This method will be removed in a future release.');

    if (docs) {
      console.warn('For more information about usage see ' + docs);
    }
  } catch (e) { /* Ignore */ }
};

```

### node_modules\axios\lib\helpers\isAbsoluteURL.js
```javascript
'use strict';

/**
 * Determines whether the specified URL is absolute
 *
 * @param {string} url The URL to test
 * @returns {boolean} True if the specified URL is absolute, otherwise false
 */
module.exports = function isAbsoluteURL(url) {
  // A URL is considered absolute if it begins with "<scheme>://" or "//" (protocol-relative URL).
  // RFC 3986 defines scheme name as a sequence of characters beginning with a letter and followed
  // by any combination of letters, digits, plus, period, or hyphen.
  return /^([a-z][a-z\d\+\-\.]*:)?\/\//i.test(url);
};

```

### node_modules\axios\lib\helpers\isAxiosError.js
```javascript
'use strict';

/**
 * Determines whether the payload is an error thrown by Axios
 *
 * @param {*} payload The value to test
 * @returns {boolean} True if the payload is an error thrown by Axios, otherwise false
 */
module.exports = function isAxiosError(payload) {
  return (typeof payload === 'object') && (payload.isAxiosError === true);
};

```

### node_modules\axios\lib\helpers\isURLSameOrigin.js
```javascript
'use strict';

var utils = require('./../utils');

module.exports = (
  utils.isStandardBrowserEnv() ?

  // Standard browser envs have full support of the APIs needed to test
  // whether the request URL is of the same origin as current location.
    (function standardBrowserEnv() {
      var msie = /(msie|trident)/i.test(navigator.userAgent);
      var urlParsingNode = document.createElement('a');
      var originURL;

      /**
    * Parse a URL to discover it's components
    *
    * @param {String} url The URL to be parsed
    * @returns {Object}
    */
      function resolveURL(url) {
        var href = url;

        if (msie) {
        // IE needs attribute set twice to normalize properties
          urlParsingNode.setAttribute('href', href);
          href = urlParsingNode.href;
        }

        urlParsingNode.setAttribute('href', href);

        // urlParsingNode provides the UrlUtils interface - http://url.spec.whatwg.org/#urlutils
        return {
          href: urlParsingNode.href,
          protocol: urlParsingNode.protocol ? urlParsingNode.protocol.replace(/:$/, '') : '',
          host: urlParsingNode.host,
          search: urlParsingNode.search ? urlParsingNode.search.replace(/^\?/, '') : '',
          hash: urlParsingNode.hash ? urlParsingNode.hash.replace(/^#/, '') : '',
          hostname: urlParsingNode.hostname,
          port: urlParsingNode.port,
          pathname: (urlParsingNode.pathname.charAt(0) === '/') ?
            urlParsingNode.pathname :
            '/' + urlParsingNode.pathname
        };
      }

      originURL = resolveURL(window.location.href);

      /**
    * Determine if a URL shares the same origin as the current location
    *
    * @param {String} requestURL The URL to test
    * @returns {boolean} True if URL shares the same origin, otherwise false
    */
      return function isURLSameOrigin(requestURL) {
        var parsed = (utils.isString(requestURL)) ? resolveURL(requestURL) : requestURL;
        return (parsed.protocol === originURL.protocol &&
            parsed.host === originURL.host);
      };
    })() :

  // Non standard browser envs (web workers, react-native) lack needed support.
    (function nonStandardBrowserEnv() {
      return function isURLSameOrigin() {
        return true;
      };
    })()
);

```

### node_modules\axios\lib\helpers\normalizeHeaderName.js
```javascript
'use strict';

var utils = require('../utils');

module.exports = function normalizeHeaderName(headers, normalizedName) {
  utils.forEach(headers, function processHeader(value, name) {
    if (name !== normalizedName && name.toUpperCase() === normalizedName.toUpperCase()) {
      headers[normalizedName] = value;
      delete headers[name];
    }
  });
};

```

### node_modules\axios\lib\helpers\parseHeaders.js
```javascript
'use strict';

var utils = require('./../utils');

// Headers whose duplicates are ignored by node
// c.f. https://nodejs.org/api/http.html#http_message_headers
var ignoreDuplicateOf = [
  'age', 'authorization', 'content-length', 'content-type', 'etag',
  'expires', 'from', 'host', 'if-modified-since', 'if-unmodified-since',
  'last-modified', 'location', 'max-forwards', 'proxy-authorization',
  'referer', 'retry-after', 'user-agent'
];

/**
 * Parse headers into an object
 *
 * ```
 * Date: Wed, 27 Aug 2014 08:58:49 GMT
 * Content-Type: application/json
 * Connection: keep-alive
 * Transfer-Encoding: chunked
 * ```
 *
 * @param {String} headers Headers needing to be parsed
 * @returns {Object} Headers parsed into an object
 */
module.exports = function parseHeaders(headers) {
  var parsed = {};
  var key;
  var val;
  var i;

  if (!headers) { return parsed; }

  utils.forEach(headers.split('\n'), function parser(line) {
    i = line.indexOf(':');
    key = utils.trim(line.substr(0, i)).toLowerCase();
    val = utils.trim(line.substr(i + 1));

    if (key) {
      if (parsed[key] && ignoreDuplicateOf.indexOf(key) >= 0) {
        return;
      }
      if (key === 'set-cookie') {
        parsed[key] = (parsed[key] ? parsed[key] : []).concat([val]);
      } else {
        parsed[key] = parsed[key] ? parsed[key] + ', ' + val : val;
      }
    }
  });

  return parsed;
};

```

### node_modules\axios\lib\helpers\spread.js
```javascript
'use strict';

/**
 * Syntactic sugar for invoking a function and expanding an array for arguments.
 *
 * Common use case would be to use `Function.prototype.apply`.
 *
 *  ```js
 *  function f(x, y, z) {}
 *  var args = [1, 2, 3];
 *  f.apply(null, args);
 *  ```
 *
 * With `spread` this example can be re-written.
 *
 *  ```js
 *  spread(function(x, y, z) {})([1, 2, 3]);
 *  ```
 *
 * @param {Function} callback
 * @returns {Function}
 */
module.exports = function spread(callback) {
  return function wrap(arr) {
    return callback.apply(null, arr);
  };
};

```

### node_modules\axios\lib\helpers\validator.js
```javascript
'use strict';

var pkg = require('./../../package.json');

var validators = {};

// eslint-disable-next-line func-names
['object', 'boolean', 'number', 'function', 'string', 'symbol'].forEach(function(type, i) {
  validators[type] = function validator(thing) {
    return typeof thing === type || 'a' + (i < 1 ? 'n ' : ' ') + type;
  };
});

var deprecatedWarnings = {};
var currentVerArr = pkg.version.split('.');

/**
 * Compare package versions
 * @param {string} version
 * @param {string?} thanVersion
 * @returns {boolean}
 */
function isOlderVersion(version, thanVersion) {
  var pkgVersionArr = thanVersion ? thanVersion.split('.') : currentVerArr;
  var destVer = version.split('.');
  for (var i = 0; i < 3; i++) {
    if (pkgVersionArr[i] > destVer[i]) {
      return true;
    } else if (pkgVersionArr[i] < destVer[i]) {
      return false;
    }
  }
  return false;
}

/**
 * Transitional option validator
 * @param {function|boolean?} validator
 * @param {string?} version
 * @param {string} message
 * @returns {function}
 */
validators.transitional = function transitional(validator, version, message) {
  var isDeprecated = version && isOlderVersion(version);

  function formatMessage(opt, desc) {
    return '[Axios v' + pkg.version + '] Transitional option \'' + opt + '\'' + desc + (message ? '. ' + message : '');
  }

  // eslint-disable-next-line func-names
  return function(value, opt, opts) {
    if (validator === false) {
      throw new Error(formatMessage(opt, ' has been removed in ' + version));
    }

    if (isDeprecated && !deprecatedWarnings[opt]) {
      deprecatedWarnings[opt] = true;
      // eslint-disable-next-line no-console
      console.warn(
        formatMessage(
          opt,
          ' has been deprecated since v' + version + ' and will be removed in the near future'
        )
      );
    }

    return validator ? validator(value, opt, opts) : true;
  };
};

/**
 * Assert object's properties type
 * @param {object} options
 * @param {object} schema
 * @param {boolean?} allowUnknown
 */

function assertOptions(options, schema, allowUnknown) {
  if (typeof options !== 'object') {
    throw new TypeError('options must be an object');
  }
  var keys = Object.keys(options);
  var i = keys.length;
  while (i-- > 0) {
    var opt = keys[i];
    var validator = schema[opt];
    if (validator) {
      var value = options[opt];
      var result = value === undefined || validator(value, opt, options);
      if (result !== true) {
        throw new TypeError('option ' + opt + ' must be ' + result);
      }
      continue;
    }
    if (allowUnknown !== true) {
      throw Error('Unknown option ' + opt);
    }
  }
}

module.exports = {
  isOlderVersion: isOlderVersion,
  assertOptions: assertOptions,
  validators: validators
};

```

### node_modules\axios\lib\utils.js
```javascript
'use strict';

var bind = require('./helpers/bind');

// utils is a library of generic helper functions non-specific to axios

var toString = Object.prototype.toString;

/**
 * Determine if a value is an Array
 *
 * @param {Object} val The value to test
 * @returns {boolean} True if value is an Array, otherwise false
 */
function isArray(val) {
  return toString.call(val) === '[object Array]';
}

/**
 * Determine if a value is undefined
 *
 * @param {Object} val The value to test
 * @returns {boolean} True if the value is undefined, otherwise false
 */
function isUndefined(val) {
  return typeof val === 'undefined';
}

/**
 * Determine if a value is a Buffer
 *
 * @param {Object} val The value to test
 * @returns {boolean} True if value is a Buffer, otherwise false
 */
function isBuffer(val) {
  return val !== null && !isUndefined(val) && val.constructor !== null && !isUndefined(val.constructor)
    && typeof val.constructor.isBuffer === 'function' && val.constructor.isBuffer(val);
}

/**
 * Determine if a value is an ArrayBuffer
 *
 * @param {Object} val The value to test
 * @returns {boolean} True if value is an ArrayBuffer, otherwise false
 */
function isArrayBuffer(val) {
  return toString.call(val) === '[object ArrayBuffer]';
}

/**
 * Determine if a value is a FormData
 *
 * @param {Object} val The value to test
 * @returns {boolean} True if value is an FormData, otherwise false
 */
function isFormData(val) {
  return (typeof FormData !== 'undefined') && (val instanceof FormData);
}

/**
 * Determine if a value is a view on an ArrayBuffer
 *
 * @param {Object} val The value to test
 * @returns {boolean} True if value is a view on an ArrayBuffer, otherwise false
 */
function isArrayBufferView(val) {
  var result;
  if ((typeof ArrayBuffer !== 'undefined') && (ArrayBuffer.isView)) {
    result = ArrayBuffer.isView(val);
  } else {
    result = (val) && (val.buffer) && (val.buffer instanceof ArrayBuffer);
  }
  return result;
}

/**
 * Determine if a value is a String
 *
 * @param {Object} val The value to test
 * @returns {boolean} True if value is a String, otherwise false
 */
function isString(val) {
  return typeof val === 'string';
}

/**
 * Determine if a value is a Number
 *
 * @param {Object} val The value to test
 * @returns {boolean} True if value is a Number, otherwise false
 */
function isNumber(val) {
  return typeof val === 'number';
}

/**
 * Determine if a value is an Object
 *
 * @param {Object} val The value to test
 * @returns {boolean} True if value is an Object, otherwise false
 */
function isObject(val) {
  return val !== null && typeof val === 'object';
}

/**
 * Determine if a value is a plain Object
 *
 * @param {Object} val The value to test
 * @return {boolean} True if value is a plain Object, otherwise false
 */
function isPlainObject(val) {
  if (toString.call(val) !== '[object Object]') {
    return false;
  }

  var prototype = Object.getPrototypeOf(val);
  return prototype === null || prototype === Object.prototype;
}

/**
 * Determine if a value is a Date
 *
 * @param {Object} val The value to test
 * @returns {boolean} True if value is a Date, otherwise false
 */
function isDate(val) {
  return toString.call(val) === '[object Date]';
}

/**
 * Determine if a value is a File
 *
 * @param {Object} val The value to test
 * @returns {boolean} True if value is a File, otherwise false
 */
function isFile(val) {
  return toString.call(val) === '[object File]';
}

/**
 * Determine if a value is a Blob
 *
 * @param {Object} val The value to test
 * @returns {boolean} True if value is a Blob, otherwise false
 */
function isBlob(val) {
  return toString.call(val) === '[object Blob]';
}

/**
 * Determine if a value is a Function
 *
 * @param {Object} val The value to test
 * @returns {boolean} True if value is a Function, otherwise false
 */
function isFunction(val) {
  return toString.call(val) === '[object Function]';
}

/**
 * Determine if a value is a Stream
 *
 * @param {Object} val The value to test
 * @returns {boolean} True if value is a Stream, otherwise false
 */
function isStream(val) {
  return isObject(val) && isFunction(val.pipe);
}

/**
 * Determine if a value is a URLSearchParams object
 *
 * @param {Object} val The value to test
 * @returns {boolean} True if value is a URLSearchParams object, otherwise false
 */
function isURLSearchParams(val) {
  return typeof URLSearchParams !== 'undefined' && val instanceof URLSearchParams;
}

/**
 * Trim excess whitespace off the beginning and end of a string
 *
 * @param {String} str The String to trim
 * @returns {String} The String freed of excess whitespace
 */
function trim(str) {
  return str.trim ? str.trim() : str.replace(/^\s+|\s+$/g, '');
}

/**
 * Determine if we're running in a standard browser environment
 *
 * This allows axios to run in a web worker, and react-native.
 * Both environments support XMLHttpRequest, but not fully standard globals.
 *
 * web workers:
 *  typeof window -> undefined
 *  typeof document -> undefined
 *
 * react-native:
 *  navigator.product -> 'ReactNative'
 * nativescript
 *  navigator.product -> 'NativeScript' or 'NS'
 */
function isStandardBrowserEnv() {
  if (typeof navigator !== 'undefined' && (navigator.product === 'ReactNative' ||
                                           navigator.product === 'NativeScript' ||
                                           navigator.product === 'NS')) {
    return false;
  }
  return (
    typeof window !== 'undefined' &&
    typeof document !== 'undefined'
  );
}

/**
 * Iterate over an Array or an Object invoking a function for each item.
 *
 * If `obj` is an Array callback will be called passing
 * the value, index, and complete array for each item.
 *
 * If 'obj' is an Object callback will be called passing
 * the value, key, and complete object for each property.
 *
 * @param {Object|Array} obj The object to iterate
 * @param {Function} fn The callback to invoke for each item
 */
function forEach(obj, fn) {
  // Don't bother if no value provided
  if (obj === null || typeof obj === 'undefined') {
    return;
  }

  // Force an array if not already something iterable
  if (typeof obj !== 'object') {
    /*eslint no-param-reassign:0*/
    obj = [obj];
  }

  if (isArray(obj)) {
    // Iterate over array values
    for (var i = 0, l = obj.length; i < l; i++) {
      fn.call(null, obj[i], i, obj);
    }
  } else {
    // Iterate over object keys
    for (var key in obj) {
      if (Object.prototype.hasOwnProperty.call(obj, key)) {
        fn.call(null, obj[key], key, obj);
      }
    }
  }
}

/**
 * Accepts varargs expecting each argument to be an object, then
 * immutably merges the properties of each object and returns result.
 *
 * When multiple objects contain the same key the later object in
 * the arguments list will take precedence.
 *
 * Example:
 *
 * ```js
 * var result = merge({foo: 123}, {foo: 456});
 * console.log(result.foo); // outputs 456
 * ```
 *
 * @param {Object} obj1 Object to merge
 * @returns {Object} Result of all merge properties
 */
function merge(/* obj1, obj2, obj3, ... */) {
  var result = {};
  function assignValue(val, key) {
    if (isPlainObject(result[key]) && isPlainObject(val)) {
      result[key] = merge(result[key], val);
    } else if (isPlainObject(val)) {
      result[key] = merge({}, val);
    } else if (isArray(val)) {
      result[key] = val.slice();
    } else {
      result[key] = val;
    }
  }

  for (var i = 0, l = arguments.length; i < l; i++) {
    forEach(arguments[i], assignValue);
  }
  return result;
}

/**
 * Extends object a by mutably adding to it the properties of object b.
 *
 * @param {Object} a The object to be extended
 * @param {Object} b The object to copy properties from
 * @param {Object} thisArg The object to bind function to
 * @return {Object} The resulting value of object a
 */
function extend(a, b, thisArg) {
  forEach(b, function assignValue(val, key) {
    if (thisArg && typeof val === 'function') {
      a[key] = bind(val, thisArg);
    } else {
      a[key] = val;
    }
  });
  return a;
}

/**
 * Remove byte order marker. This catches EF BB BF (the UTF-8 BOM)
 *
 * @param {string} content with BOM
 * @return {string} content value without BOM
 */
function stripBOM(content) {
  if (content.charCodeAt(0) === 0xFEFF) {
    content = content.slice(1);
  }
  return content;
}

module.exports = {
  isArray: isArray,
  isArrayBuffer: isArrayBuffer,
  isBuffer: isBuffer,
  isFormData: isFormData,
  isArrayBufferView: isArrayBufferView,
  isString: isString,
  isNumber: isNumber,
  isObject: isObject,
  isPlainObject: isPlainObject,
  isUndefined: isUndefined,
  isDate: isDate,
  isFile: isFile,
  isBlob: isBlob,
  isFunction: isFunction,
  isStream: isStream,
  isURLSearchParams: isURLSearchParams,
  isStandardBrowserEnv: isStandardBrowserEnv,
  forEach: forEach,
  merge: merge,
  extend: extend,
  trim: trim,
  stripBOM: stripBOM
};

```

### node_modules\axios\package.json
```json
{
  "name": "axios",
  "version": "0.21.4",
  "description": "Promise based HTTP client for the browser and node.js",
  "main": "index.js",
  "scripts": {
    "test": "grunt test",
    "start": "node ./sandbox/server.js",
    "build": "NODE_ENV=production grunt build",
    "preversion": "npm test",
    "version": "npm run build && grunt version && git add -A dist && git add CHANGELOG.md bower.json package.json",
    "postversion": "git push && git push --tags",
    "examples": "node ./examples/server.js",
    "coveralls": "cat coverage/lcov.info | ./node_modules/coveralls/bin/coveralls.js",
    "fix": "eslint --fix lib/**/*.js"
  },
  "repository": {
    "type": "git",
    "url": "https://github.com/axios/axios.git"
  },
  "keywords": [
    "xhr",
    "http",
    "ajax",
    "promise",
    "node"
  ],
  "author": "Matt Zabriskie",
  "license": "MIT",
  "bugs": {
    "url": "https://github.com/axios/axios/issues"
  },
  "homepage": "https://axios-http.com",
  "devDependencies": {
    "coveralls": "^3.0.0",
    "es6-promise": "^4.2.4",
    "grunt": "^1.3.0",
    "grunt-banner": "^0.6.0",
    "grunt-cli": "^1.2.0",
    "grunt-contrib-clean": "^1.1.0",
    "grunt-contrib-watch": "^1.0.0",
    "grunt-eslint": "^23.0.0",
    "grunt-karma": "^4.0.0",
    "grunt-mocha-test": "^0.13.3",
    "grunt-ts": "^6.0.0-beta.19",
    "grunt-webpack": "^4.0.2",
    "istanbul-instrumenter-loader": "^1.0.0",
    "jasmine-core": "^2.4.1",
    "karma": "^6.3.2",
    "karma-chrome-launcher": "^3.1.0",
    "karma-firefox-launcher": "^2.1.0",
    "karma-jasmine": "^1.1.1",
    "karma-jasmine-ajax": "^0.1.13",
    "karma-safari-launcher": "^1.0.0",
    "karma-sauce-launcher": "^4.3.6",
    "karma-sinon": "^1.0.5",
    "karma-sourcemap-loader": "^0.3.8",
    "karma-webpack": "^4.0.2",
    "load-grunt-tasks": "^3.5.2",
    "minimist": "^1.2.0",
    "mocha": "^8.2.1",
    "sinon": "^4.5.0",
    "terser-webpack-plugin": "^4.2.3",
    "typescript": "^4.0.5",
    "url-search-params": "^0.10.0",
    "webpack": "^4.44.2",
    "webpack-dev-server": "^3.11.0"
  },
  "browser": {
    "./lib/adapters/http.js": "./lib/adapters/xhr.js"
  },
  "jsdelivr": "dist/axios.min.js",
  "unpkg": "dist/axios.min.js",
  "typings": "./index.d.ts",
  "dependencies": {
    "follow-redirects": "^1.14.0"
  },
  "bundlesize": [
    {
      "path": "./dist/axios.min.js",
      "threshold": "5kB"
    }
  ]
}

```

### node_modules\follow-redirects\README.md
```markdown
## Follow Redirects

Drop-in replacement for Node's `http` and `https` modules that automatically follows redirects.

[![npm version](https://img.shields.io/npm/v/follow-redirects.svg)](https://www.npmjs.com/package/follow-redirects)
[![Build Status](https://github.com/follow-redirects/follow-redirects/workflows/CI/badge.svg)](https://github.com/follow-redirects/follow-redirects/actions)
[![Coverage Status](https://coveralls.io/repos/follow-redirects/follow-redirects/badge.svg?branch=master)](https://coveralls.io/r/follow-redirects/follow-redirects?branch=master)
[![npm downloads](https://img.shields.io/npm/dm/follow-redirects.svg)](https://www.npmjs.com/package/follow-redirects)
[![Sponsor on GitHub](https://img.shields.io/static/v1?label=Sponsor&message=%F0%9F%92%96&logo=GitHub)](https://github.com/sponsors/RubenVerborgh)

`follow-redirects` provides [request](https://nodejs.org/api/http.html#http_http_request_options_callback) and [get](https://nodejs.org/api/http.html#http_http_get_options_callback)
 methods that behave identically to those found on the native [http](https://nodejs.org/api/http.html#http_http_request_options_callback) and [https](https://nodejs.org/api/https.html#https_https_request_options_callback)
 modules, with the exception that they will seamlessly follow redirects.

```javascript
const { http, https } = require('follow-redirects');

http.get('http://bit.ly/900913', response => {
  response.on('data', chunk => {
    console.log(chunk);
  });
}).on('error', err => {
  console.error(err);
});
```

You can inspect the final redirected URL through the `responseUrl` property on the `response`.
If no redirection happened, `responseUrl` is the original request URL.

```javascript
const request = https.request({
  host: 'bitly.com',
  path: '/UHfDGO',
}, response => {
  console.log(response.responseUrl);
  // 'http://duckduckgo.com/robots.txt'
});
request.end();
```

## Options
### Global options
Global options are set directly on the `follow-redirects` module:

```javascript
const followRedirects = require('follow-redirects');
followRedirects.maxRedirects = 10;
followRedirects.maxBodyLength = 20 * 1024 * 1024; // 20 MB
```

The following global options are supported:

- `maxRedirects` (default: `21`) – sets the maximum number of allowed redirects; if exceeded, an error will be emitted.

- `maxBodyLength` (default: 10MB) – sets the maximum size of the request body; if exceeded, an error will be emitted.

### Per-request options
Per-request options are set by passing an `options` object:

```javascript
const url = require('url');
const { http, https } = require('follow-redirects');

const options = url.parse('http://bit.ly/900913');
options.maxRedirects = 10;
options.beforeRedirect = (options, response, request) => {
  // Use this to adjust the request options upon redirecting,
  // to inspect the latest response headers,
  // or to cancel the request by throwing an error

  // response.headers = the redirect response headers
  // response.statusCode = the redirect response code (eg. 301, 307, etc.)

  // request.url = the requested URL that resulted in a redirect
  // request.headers = the headers in the request that resulted in a redirect
  // request.method = the method of the request that resulted in a redirect
  if (options.hostname === "example.com") {
    options.auth = "user:password";
  }
};
http.request(options);
```

In addition to the [standard HTTP](https://nodejs.org/api/http.html#http_http_request_options_callback) and [HTTPS options](https://nodejs.org/api/https.html#https_https_request_options_callback),
the following per-request options are supported:
- `followRedirects` (default: `true`) – whether redirects should be followed.

- `maxRedirects` (default: `21`) – sets the maximum number of allowed redirects; if exceeded, an error will be emitted.

- `maxBodyLength` (default: 10MB) – sets the maximum size of the request body; if exceeded, an error will be emitted.

- `beforeRedirect` (default: `undefined`) – optionally change the request `options` on redirects, or abort the request by throwing an error.

- `agents` (default: `undefined`) – sets the `agent` option per protocol, since HTTP and HTTPS use different agents. Example value: `{ http: new http.Agent(), https: new https.Agent() }`

- `trackRedirects` (default: `false`) – whether to store the redirected response details into the `redirects` array on the response object.


### Advanced usage
By default, `follow-redirects` will use the Node.js default implementations
of [`http`](https://nodejs.org/api/http.html)
and [`https`](https://nodejs.org/api/https.html).
To enable features such as caching and/or intermediate request tracking,
you might instead want to wrap `follow-redirects` around custom protocol implementations:

```javascript
const { http, https } = require('follow-redirects').wrap({
  http: require('your-custom-http'),
  https: require('your-custom-https'),
});
```

Such custom protocols only need an implementation of the `request` method.

## Browser Usage

Due to the way the browser works,
the `http` and `https` browser equivalents perform redirects by default.

By requiring `follow-redirects` this way:
```javascript
const http = require('follow-redirects/http');
const https = require('follow-redirects/https');
```
you can easily tell webpack and friends to replace
`follow-redirect` by the built-in versions:

```json
{
  "follow-redirects/http"  : "http",
  "follow-redirects/https" : "https"
}
```

## Contributing

Pull Requests are always welcome. Please [file an issue](https://github.com/follow-redirects/follow-redirects/issues)
 detailing your proposal before you invest your valuable time. Additional features and bug fixes should be accompanied
 by tests. You can run the test suite locally with a simple `npm test` command.

## Debug Logging

`follow-redirects` uses the excellent [debug](https://www.npmjs.com/package/debug) for logging. To turn on logging
 set the environment variable `DEBUG=follow-redirects` for debug output from just this module. When running the test
 suite it is sometimes advantageous to set `DEBUG=*` to see output from the express server as well.

## Authors

- [Ruben Verborgh](https://ruben.verborgh.org/)
- [Olivier Lalonde](mailto:olalonde@gmail.com)
- [James Talmage](mailto:james@talmage.io)

## License

[MIT License](https://github.com/follow-redirects/follow-redirects/blob/master/LICENSE)

```

### node_modules\follow-redirects\debug.js
```javascript
var debug;

module.exports = function () {
  if (!debug) {
    try {
      /* eslint global-require: off */
      debug = require("debug")("follow-redirects");
    }
    catch (error) { /* */ }
    if (typeof debug !== "function") {
      debug = function () { /* */ };
    }
  }
  debug.apply(null, arguments);
};

```

### node_modules\follow-redirects\http.js
```javascript
module.exports = require("follow-redirects").http;

```

### node_modules\follow-redirects\https.js
```javascript
module.exports = require("./").https;

```

### node_modules\follow-redirects\index.js
```javascript
var url = require("url");
var URL = url.URL;
var http = require("http");
var https = require("https");
var Writable = require("stream").Writable;
var assert = require("assert");
var debug = require("follow-redirects/debug");

// Preventive platform detection
// istanbul ignore next
(function detectUnsupportedEnvironment() {
  var looksLikeNode = typeof process !== "undefined";
  var looksLikeBrowser = typeof window !== "undefined" && typeof document !== "undefined";
  var looksLikeV8 = isFunction(Error.captureStackTrace);
  if (!looksLikeNode && (looksLikeBrowser || !looksLikeV8)) {
    console.warn("The follow-redirects package should be excluded from browser builds.");
  }
}());

// Whether to use the native URL object or the legacy url module
var useNativeURL = false;
try {
  assert(new URL(""));
}
catch (error) {
  useNativeURL = error.code === "ERR_INVALID_URL";
}

// URL fields to preserve in copy operations
var preservedUrlFields = [
  "auth",
  "host",
  "hostname",
  "href",
  "path",
  "pathname",
  "port",
  "protocol",
  "query",
  "search",
  "hash",
];

// Create handlers that pass events from native requests
var events = ["abort", "aborted", "connect", "error", "socket", "timeout"];
var eventHandlers = Object.create(null);
events.forEach(function (event) {
  eventHandlers[event] = function (arg1, arg2, arg3) {
    this._redirectable.emit(event, arg1, arg2, arg3);
  };
});

// Error types with codes
var InvalidUrlError = createErrorType(
  "ERR_INVALID_URL",
  "Invalid URL",
  TypeError
);
var RedirectionError = createErrorType(
  "ERR_FR_REDIRECTION_FAILURE",
  "Redirected request failed"
);
var TooManyRedirectsError = createErrorType(
  "ERR_FR_TOO_MANY_REDIRECTS",
  "Maximum number of redirects exceeded",
  RedirectionError
);
var MaxBodyLengthExceededError = createErrorType(
  "ERR_FR_MAX_BODY_LENGTH_EXCEEDED",
  "Request body larger than maxBodyLength limit"
);
var WriteAfterEndError = createErrorType(
  "ERR_STREAM_WRITE_AFTER_END",
  "write after end"
);

// istanbul ignore next
var destroy = Writable.prototype.destroy || noop;

// An HTTP(S) request that can be redirected
function RedirectableRequest(options, responseCallback) {
  // Initialize the request
  Writable.call(this);
  this._sanitizeOptions(options);
  this._options = options;
  this._ended = false;
  this._ending = false;
  this._redirectCount = 0;
  this._redirects = [];
  this._requestBodyLength = 0;
  this._requestBodyBuffers = [];

  // Attach a callback if passed
  if (responseCallback) {
    this.on("response", responseCallback);
  }

  // React to responses of native requests
  var self = this;
  this._onNativeResponse = function (response) {
    try {
      self._processResponse(response);
    }
    catch (cause) {
      self.emit("error", cause instanceof RedirectionError ?
        cause : new RedirectionError({ cause: cause }));
    }
  };

  // Perform the first request
  this._performRequest();
}
RedirectableRequest.prototype = Object.create(Writable.prototype);

RedirectableRequest.prototype.abort = function () {
  destroyRequest(this._currentRequest);
  this._currentRequest.abort();
  this.emit("abort");
};

RedirectableRequest.prototype.destroy = function (error) {
  destroyRequest(this._currentRequest, error);
  destroy.call(this, error);
  return this;
};

// Writes buffered data to the current native request
RedirectableRequest.prototype.write = function (data, encoding, callback) {
  // Writing is not allowed if end has been called
  if (this._ending) {
    throw new WriteAfterEndError();
  }

  // Validate input and shift parameters if necessary
  if (!isString(data) && !isBuffer(data)) {
    throw new TypeError("data should be a string, Buffer or Uint8Array");
  }
  if (isFunction(encoding)) {
    callback = encoding;
    encoding = null;
  }

  // Ignore empty buffers, since writing them doesn't invoke the callback
  // https://github.com/nodejs/node/issues/22066
  if (data.length === 0) {
    if (callback) {
      callback();
    }
    return;
  }
  // Only write when we don't exceed the maximum body length
  if (this._requestBodyLength + data.length <= this._options.maxBodyLength) {
    this._requestBodyLength += data.length;
    this._requestBodyBuffers.push({ data: data, encoding: encoding });
    this._currentRequest.write(data, encoding, callback);
  }
  // Error when we exceed the maximum body length
  else {
    this.emit("error", new MaxBodyLengthExceededError());
    this.abort();
  }
};

// Ends the current native request
RedirectableRequest.prototype.end = function (data, encoding, callback) {
  // Shift parameters if necessary
  if (isFunction(data)) {
    callback = data;
    data = encoding = null;
  }
  else if (isFunction(encoding)) {
    callback = encoding;
    encoding = null;
  }

  // Write data if needed and end
  if (!data) {
    this._ended = this._ending = true;
    this._currentRequest.end(null, null, callback);
  }
  else {
    var self = this;
    var currentRequest = this._currentRequest;
    this.write(data, encoding, function () {
      self._ended = true;
      currentRequest.end(null, null, callback);
    });
    this._ending = true;
  }
};

// Sets a header value on the current native request
RedirectableRequest.prototype.setHeader = function (name, value) {
  this._options.headers[name] = value;
  this._currentRequest.setHeader(name, value);
};

// Clears a header value on the current native request
RedirectableRequest.prototype.removeHeader = function (name) {
  delete this._options.headers[name];
  this._currentRequest.removeHeader(name);
};

// Global timeout for all underlying requests
RedirectableRequest.prototype.setTimeout = function (msecs, callback) {
  var self = this;

  // Destroys the socket on timeout
  function destroyOnTimeout(socket) {
    socket.setTimeout(msecs);
    socket.removeListener("timeout", socket.destroy);
    socket.addListener("timeout", socket.destroy);
  }

  // Sets up a timer to trigger a timeout event
  function startTimer(socket) {
    if (self._timeout) {
      clearTimeout(self._timeout);
    }
    self._timeout = setTimeout(function () {
      self.emit("timeout");
      clearTimer();
    }, msecs);
    destroyOnTimeout(socket);
  }

  // Stops a timeout from triggering
  function clearTimer() {
    // Clear the timeout
    if (self._timeout) {
      clearTimeout(self._timeout);
      self._timeout = null;
    }

    // Clean up all attached listeners
    self.removeListener("abort", clearTimer);
    self.removeListener("error", clearTimer);
    self.removeListener("response", clearTimer);
    self.removeListener("close", clearTimer);
    if (callback) {
      self.removeListener("timeout", callback);
    }
    if (!self.socket) {
      self._currentRequest.removeListener("socket", startTimer);
    }
  }

  // Attach callback if passed
  if (callback) {
    this.on("timeout", callback);
  }

  // Start the timer if or when the socket is opened
  if (this.socket) {
    startTimer(this.socket);
  }
  else {
    this._currentRequest.once("socket", startTimer);
  }

  // Clean up on events
  this.on("socket", destroyOnTimeout);
  this.on("abort", clearTimer);
  this.on("error", clearTimer);
  this.on("response", clearTimer);
  this.on("close", clearTimer);

  return this;
};

// Proxy all other public ClientRequest methods
[
  "flushHeaders", "getHeader",
  "setNoDelay", "setSocketKeepAlive",
].forEach(function (method) {
  RedirectableRequest.prototype[method] = function (a, b) {
    return this._currentRequest[method](a, b);
  };
});

// Proxy all public ClientRequest properties
["aborted", "connection", "socket"].forEach(function (property) {
  Object.defineProperty(RedirectableRequest.prototype, property, {
    get: function () { return this._currentRequest[property]; },
  });
});

RedirectableRequest.prototype._sanitizeOptions = function (options) {
  // Ensure headers are always present
  if (!options.headers) {
    options.headers = {};
  }

  // Since http.request treats host as an alias of hostname,
  // but the url module interprets host as hostname plus port,
  // eliminate the host property to avoid confusion.
  if (options.host) {
    // Use hostname if set, because it has precedence
    if (!options.hostname) {
      options.hostname = options.host;
    }
    delete options.host;
  }

  // Complete the URL object when necessary
  if (!options.pathname && options.path) {
    var searchPos = options.path.indexOf("?");
    if (searchPos < 0) {
      options.pathname = options.path;
    }
    else {
      options.pathname = options.path.substring(0, searchPos);
      options.search = options.path.substring(searchPos);
    }
  }
};


// Executes the next native request (initial or redirect)
RedirectableRequest.prototype._performRequest = function () {
  // Load the native protocol
  var protocol = this._options.protocol;
  var nativeProtocol = this._options.nativeProtocols[protocol];
  if (!nativeProtocol) {
    throw new TypeError("Unsupported protocol " + protocol);
  }

  // If specified, use the agent corresponding to the protocol
  // (HTTP and HTTPS use different types of agents)
  if (this._options.agents) {
    var scheme = protocol.slice(0, -1);
    this._options.agent = this._options.agents[scheme];
  }

  // Create the native request and set up its event handlers
  var request = this._currentRequest =
    nativeProtocol.request(this._options, this._onNativeResponse);
  request._redirectable = this;
  for (var event of events) {
    request.on(event, eventHandlers[event]);
  }

  // RFC7230§5.3.1: When making a request directly to an origin server, […]
  // a client MUST send only the absolute path […] as the request-target.
  this._currentUrl = /^\//.test(this._options.path) ?
    url.format(this._options) :
    // When making a request to a proxy, […]
    // a client MUST send the target URI in absolute-form […].
    this._options.path;

  // End a redirected request
  // (The first request must be ended explicitly with RedirectableRequest#end)
  if (this._isRedirect) {
    // Write the request entity and end
    var i = 0;
    var self = this;
    var buffers = this._requestBodyBuffers;
    (function writeNext(error) {
      // Only write if this request has not been redirected yet
      // istanbul ignore else
      if (request === self._currentRequest) {
        // Report any write errors
        // istanbul ignore if
        if (error) {
          self.emit("error", error);
        }
        // Write the next buffer if there are still left
        else if (i < buffers.length) {
          var buffer = buffers[i++];
          // istanbul ignore else
          if (!request.finished) {
            request.write(buffer.data, buffer.encoding, writeNext);
          }
        }
        // End the request if `end` has been called on us
        else if (self._ended) {
          request.end();
        }
      }
    }());
  }
};

// Processes a response from the current native request
RedirectableRequest.prototype._processResponse = function (response) {
  // Store the redirected response
  var statusCode = response.statusCode;
  if (this._options.trackRedirects) {
    this._redirects.push({
      url: this._currentUrl,
      headers: response.headers,
      statusCode: statusCode,
    });
  }

  // RFC7231§6.4: The 3xx (Redirection) class of status code indicates
  // that further action needs to be taken by the user agent in order to
  // fulfill the request. If a Location header field is provided,
  // the user agent MAY automatically redirect its request to the URI
  // referenced by the Location field value,
  // even if the specific status code is not understood.

  // If the response is not a redirect; return it as-is
  var location = response.headers.location;
  if (!location || this._options.followRedirects === false ||
    statusCode < 300 || statusCode >= 400) {
    response.responseUrl = this._currentUrl;
    response.redirects = this._redirects;
    this.emit("response", response);

    // Clean up
    this._requestBodyBuffers = [];
    return;
  }

  // The response is a redirect, so abort the current request
  destroyRequest(this._currentRequest);
  // Discard the remainder of the response to avoid waiting for data
  response.destroy();

  // RFC7231§6.4: A client SHOULD detect and intervene
  // in cyclical redirections (i.e., "infinite" redirection loops).
  if (++this._redirectCount > this._options.maxRedirects) {
    throw new TooManyRedirectsError();
  }

  // Store the request headers if applicable
  var requestHeaders;
  var beforeRedirect = this._options.beforeRedirect;
  if (beforeRedirect) {
    requestHeaders = Object.assign({
      // The Host header was set by nativeProtocol.request
      Host: response.req.getHeader("host"),
    }, this._options.headers);
  }

  // RFC7231§6.4: Automatic redirection needs to done with
  // care for methods not known to be safe, […]
  // RFC7231§6.4.2–3: For historical reasons, a user agent MAY change
  // the request method from POST to GET for the subsequent request.
  var method = this._options.method;
  if ((statusCode === 301 || statusCode === 302) && this._options.method === "POST" ||
    // RFC7231§6.4.4: The 303 (See Other) status code indicates that
    // the server is redirecting the user agent to a different resource […]
    // A user agent can perform a retrieval request targeting that URI
    // (a GET or HEAD request if using HTTP) […]
    (statusCode === 303) && !/^(?:GET|HEAD)$/.test(this._options.method)) {
    this._options.method = "GET";
    // Drop a possible entity and headers related to it
    this._requestBodyBuffers = [];
    removeMatchingHeaders(/^content-/i, this._options.headers);
  }

  // Drop the Host header, as the redirect might lead to a different host
  var currentHostHeader = removeMatchingHeaders(/^host$/i, this._options.headers);

  // If the redirect is relative, carry over the host of the last request
  var currentUrlParts = parseUrl(this._currentUrl);
  var currentHost = currentHostHeader || currentUrlParts.host;
  var currentUrl = /^\w+:/.test(location) ? this._currentUrl :
    url.format(Object.assign(currentUrlParts, { host: currentHost }));

  // Create the redirected request
  var redirectUrl = resolveUrl(location, currentUrl);
  debug("redirecting to", redirectUrl.href);
  this._isRedirect = true;
  spreadUrlObject(redirectUrl, this._options);

  // Drop confidential headers when redirecting to a less secure protocol
  // or to a different domain that is not a superdomain
  if (redirectUrl.protocol !== currentUrlParts.protocol &&
    redirectUrl.protocol !== "https:" ||
    redirectUrl.host !== currentHost &&
    !isSubdomain(redirectUrl.host, currentHost)) {
    removeMatchingHeaders(/^(?:(?:proxy-)?authorization|cookie)$/i, this._options.headers);
  }

  // Evaluate the beforeRedirect callback
  if (isFunction(beforeRedirect)) {
    var responseDetails = {
      headers: response.headers,
      statusCode: statusCode,
    };
    var requestDetails = {
      url: currentUrl,
      method: method,
      headers: requestHeaders,
    };
    beforeRedirect(this._options, responseDetails, requestDetails);
    this._sanitizeOptions(this._options);
  }

  // Perform the redirected request
  this._performRequest();
};

// Wraps the key/value object of protocols with redirect functionality
function wrap(protocols) {
  // Default settings
  var exports = {
    maxRedirects: 21,
    maxBodyLength: 10 * 1024 * 1024,
  };

  // Wrap each protocol
  var nativeProtocols = {};
  Object.keys(protocols).forEach(function (scheme) {
    var protocol = scheme + ":";
    var nativeProtocol = nativeProtocols[protocol] = protocols[scheme];
    var wrappedProtocol = exports[scheme] = Object.create(nativeProtocol);

    // Executes a request, following redirects
    function request(input, options, callback) {
      // Parse parameters, ensuring that input is an object
      if (isURL(input)) {
        input = spreadUrlObject(input);
      }
      else if (isString(input)) {
        input = spreadUrlObject(parseUrl(input));
      }
      else {
        callback = options;
        options = validateUrl(input);
        input = { protocol: protocol };
      }
      if (isFunction(options)) {
        callback = options;
        options = null;
      }

      // Set defaults
      options = Object.assign({
        maxRedirects: exports.maxRedirects,
        maxBodyLength: exports.maxBodyLength,
      }, input, options);
      options.nativeProtocols = nativeProtocols;
      if (!isString(options.host) && !isString(options.hostname)) {
        options.hostname = "::1";
      }

      assert.equal(options.protocol, protocol, "protocol mismatch");
      debug("options", options);
      return new RedirectableRequest(options, callback);
    }

    // Executes a GET request, following redirects
    function get(input, options, callback) {
      var wrappedRequest = wrappedProtocol.request(input, options, callback);
      wrappedRequest.end();
      return wrappedRequest;
    }

    // Expose the properties on the wrapped protocol
    Object.defineProperties(wrappedProtocol, {
      request: { value: request, configurable: true, enumerable: true, writable: true },
      get: { value: get, configurable: true, enumerable: true, writable: true },
    });
  });
  return exports;
}

function noop() { /* empty */ }

function parseUrl(input) {
  var parsed;
  // istanbul ignore else
  if (useNativeURL) {
    parsed = new URL(input);
  }
  else {
    // Ensure the URL is valid and absolute
    parsed = validateUrl(url.parse(input));
    if (!isString(parsed.protocol)) {
      throw new InvalidUrlError({ input });
    }
  }
  return parsed;
}

function resolveUrl(relative, base) {
  // istanbul ignore next
  return useNativeURL ? new URL(relative, base) : parseUrl(url.resolve(base, relative));
}

function validateUrl(input) {
  if (/^\[/.test(input.hostname) && !/^\[[:0-9a-f]+\]$/i.test(input.hostname)) {
    throw new InvalidUrlError({ input: input.href || input });
  }
  if (/^\[/.test(input.host) && !/^\[[:0-9a-f]+\](:\d+)?$/i.test(input.host)) {
    throw new InvalidUrlError({ input: input.href || input });
  }
  return input;
}

function spreadUrlObject(urlObject, target) {
  var spread = target || {};
  for (var key of preservedUrlFields) {
    spread[key] = urlObject[key];
  }

  // Fix IPv6 hostname
  if (spread.hostname.startsWith("[")) {
    spread.hostname = spread.hostname.slice(1, -1);
  }
  // Ensure port is a number
  if (spread.port !== "") {
    spread.port = Number(spread.port);
  }
  // Concatenate path
  spread.path = spread.search ? spread.pathname + spread.search : spread.pathname;

  return spread;
}

function removeMatchingHeaders(regex, headers) {
  var lastValue;
  for (var header in headers) {
    if (regex.test(header)) {
      lastValue = headers[header];
      delete headers[header];
    }
  }
  return (lastValue === null || typeof lastValue === "undefined") ?
    undefined : String(lastValue).trim();
}

function createErrorType(code, message, baseClass) {
  // Create constructor
  function CustomError(properties) {
    // istanbul ignore else
    if (isFunction(Error.captureStackTrace)) {
      Error.captureStackTrace(this, this.constructor);
    }
    Object.assign(this, properties || {});
    this.code = code;
    this.message = this.cause ? message + ": " + this.cause.message : message;
  }

  // Attach constructor and set default properties
  CustomError.prototype = new (baseClass || Error)();
  Object.defineProperties(CustomError.prototype, {
    constructor: {
      value: CustomError,
      enumerable: false,
    },
    name: {
      value: "Error [" + code + "]",
      enumerable: false,
    },
  });
  return CustomError;
}

function destroyRequest(request, error) {
  for (var event of events) {
    request.removeListener(event, eventHandlers[event]);
  }
  request.on("error", noop);
  request.destroy(error);
}

function isSubdomain(subdomain, domain) {
  assert(isString(subdomain) && isString(domain));
  var dot = subdomain.length - domain.length - 1;
  return dot > 0 && subdomain[dot] === "." && subdomain.endsWith(domain);
}

function isString(value) {
  return typeof value === "string" || value instanceof String;
}

function isFunction(value) {
  return typeof value === "function";
}

function isBuffer(value) {
  return typeof value === "object" && ("length" in value);
}

function isURL(value) {
  return URL && value instanceof URL;
}

// Exports
module.exports = wrap({ http: http, https: https });
module.exports.wrap = wrap;

```

### node_modules\follow-redirects\package.json
```json
{
  "name": "follow-redirects",
  "version": "1.15.9",
  "description": "HTTP and HTTPS modules that follow redirects.",
  "license": "MIT",
  "main": "index.js",
  "files": [
    "*.js"
  ],
  "engines": {
    "node": ">=4.0"
  },
  "scripts": {
    "lint": "eslint *.js test",
    "test": "nyc mocha"
  },
  "repository": {
    "type": "git",
    "url": "git+ssh://git@github.com/follow-redirects/follow-redirects.git"
  },
  "homepage": "https://github.com/follow-redirects/follow-redirects",
  "bugs": {
    "url": "https://github.com/follow-redirects/follow-redirects/issues"
  },
  "keywords": [
    "http",
    "https",
    "url",
    "redirect",
    "client",
    "location",
    "utility"
  ],
  "author": "Ruben Verborgh <ruben@verborgh.org> (https://ruben.verborgh.org/)",
  "contributors": [
    "Olivier Lalonde <olalonde@gmail.com> (http://www.syskall.com)",
    "James Talmage <james@talmage.io>"
  ],
  "funding": [
    {
      "type": "individual",
      "url": "https://github.com/sponsors/RubenVerborgh"
    }
  ],
  "peerDependenciesMeta": {
    "debug": {
      "optional": true
    }
  },
  "devDependencies": {
    "concat-stream": "^2.0.0",
    "eslint": "^5.16.0",
    "express": "^4.16.4",
    "lolex": "^3.1.0",
    "mocha": "^6.0.2",
    "nyc": "^14.1.1"
  }
}

```

### package-lock.json
```json
{
  "name": "lsdmxmp-client",
  "lockfileVersion": 3,
  "requires": true,
  "packages": {
    "": {
      "dependencies": {
        "@everdev/lsdmxmp-client": "^0.0.1-SNAPSHOT-dev"
      }
    },
    "node_modules/@everdev/lsdmxmp-client": {
      "version": "0.0.1-SNAPSHOT-dev",
      "resolved": "https://repo-everdev.nie.netease.com/repository/npm/@everdev/lsdmxmp-client/-/lsdmxmp-client-0.0.1-SNAPSHOT-dev.tgz",
      "integrity": "sha512-aIfDjE8pSlXrzSDGlGqcxmm/yTmwZZjuZefv0RPdR8N4kqbrnou2lckV2ULxV9614eBUlGeLo6IkB4Ik0rKM4g==",
      "dependencies": {
        "axios": "^0.21.1"
      }
    },
    "node_modules/axios": {
      "version": "0.21.4",
      "resolved": "https://repo-everdev.nie.netease.com/repository/npm/axios/-/axios-0.21.4.tgz",
      "integrity": "sha512-ut5vewkiu8jjGBdqpM44XxjuCjq9LAKeHVmoVfHVzy8eHgxxq8SbAVQNovDA8mVi05kP0Ea/n/UzcSHcTJQfNg==",
      "dependencies": {
        "follow-redirects": "^1.14.0"
      }
    },
    "node_modules/follow-redirects": {
      "version": "1.15.9",
      "resolved": "https://repo-everdev.nie.netease.com/repository/npm/follow-redirects/-/follow-redirects-1.15.9.tgz",
      "integrity": "sha512-gew4GsXizNgdoRyqmyfMHyAmXsZDk6mHkSxZFCzW9gwlbtOW44CDtYavM+y+72qD/Vq2l550kMF52DT8fOLJqQ==",
      "funding": [
        {
          "type": "individual",
          "url": "https://github.com/sponsors/RubenVerborgh"
        }
      ],
      "engines": {
        "node": ">=4.0"
      },
      "peerDependenciesMeta": {
        "debug": {
          "optional": true
        }
      }
    }
  }
}

```

### package.json
```json
{
  "dependencies": {
    "@everdev/lsdmxmp-client": "^0.0.1-SNAPSHOT-dev"
  }
}

```

