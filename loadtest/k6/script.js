import { check } from "k6";
import http from "k6/http";

export let options = {
    duration: "2m",
    vus: 10,
}

export default function() {
  let res = http.get("http://localhost:8080/api/v3/pet/findByStatus?status=available");
  check(res, {
    "is status 200": (r) => r.status === 200
  });
};
