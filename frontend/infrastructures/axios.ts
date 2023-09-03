import axios, { AxiosInstance } from "axios";

{
  /* 新しいAxiosインスタンスを作成して、その設定（ベースURL、ヘッダーなど）を定義*/
}
const api: AxiosInstance = axios.create({
  baseURL: process.env.NEXT_PUBLIC_API_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

{
  /*リクエストが送られる前に実行される関数を登録。現在は設定(config)をそのまま返しているが、認証トークンを追加するなどの処理を追加予定 */
}
api.interceptors.request.use(
  (config) => {
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

{
  /*レスポンスが返ってきた後に実行される関数 */
}
api.interceptors.response.use(
  (response) => {
    return response;
  },
  (error) => {
    return Promise.reject(error);
  }
);

export default api;
