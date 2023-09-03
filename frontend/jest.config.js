module.exports = {
  // Jestでテストするファイルの拡張子
  moduleFileExtensions: ["js", "json", "jsx", "ts", "tsx", "json"],

  // テスト対象ファイルのパスや正規表現
  testRegex: "(/__tests__/.*|(\\.|/)(test|spec))\\.(jsx?|tsx?|ts?)$",

  // TypeScriptをトランスパイルする設定
  transform: {
    "^.+\\.(ts|tsx)$": "ts-jest",
  },

  // テスト環境
  testEnvironment: "node",

  // モジュールのマッピング
  moduleNameMapper: {
    "^@/(.*)$": "<rootDir>/$1",
  },

  // その他の設定
  setupFiles: ["<rootDir>/jestSetup.js"],
};
