"use client";
import { useEffect, useState } from "react";

export default function RedirectURL() {
  const [longURL, setLongURL] = useState<string>();

  function handleGetLongUrl() {
    function getLastFiveCharacters(str: string) {
      return str.slice(-5);
    }
    const endpointPath = `/api/get_url?shortcode=${getLastFiveCharacters(
      window.location.pathname
    )}`;
    console.log("this", endpointPath);
    fetch(endpointPath, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((res) => res.json())
      .then((data) => {
        setLongURL(data.original_url);
        console.log(data);
      });

    if (longURL) {
      window.location.href = `http://${longURL}`;
    }
  }

  handleGetLongUrl();

  return null;
}