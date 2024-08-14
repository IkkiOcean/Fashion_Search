import React, { useState } from "react";
import axios from "axios";
import "./home.css";
import Modal from "@mui/material/Modal";
import Box from "@mui/material/Box";
import Markdown from "react-markdown";
const Home = () => {
  const [searchText, setSearchText] = useState("");
  const [searchResults, setSearchResults] = useState([]);
  const [description, setDescription] = useState();
  const [startPage, setStartPage] = useState(true);
  const [open, setOpen] = useState(false);
  const [Loading, setLoading] = useState(false);

  const handleSearchText = (value) => {
    setSearchText(value);
    if (value == "") {
      setStartPage(true);
    }
  };
  const handleClick = () => {
    if (searchText == "") {
      alert("Please enter a search term");
    } else {
      setLoading(true);
      axios
        .get(`http://127.0.0.1:5000/get-result?query=${searchText}`)
        .then((res) => {
          var resultArr = res.data;
          console.log(resultArr[0]);
          setSearchResults(resultArr);
          setStartPage(false);
          setLoading(false);
        });
    }
  };
  return (
    <>
      <div className="container">
        <div className="row1">
          <div>
            <div className="main-logo">
              <img src="./main-logo.png" alt="" />
            </div>
            <input
              type="text"
              class="formcontrol"
              placeholder="Enter your fashion related query"
              
              value={searchText}
              onChange={(event) => {
                handleSearchText(event.target.value);
                console.log(event.target.value);
              }}
            />
            <button id="upload" onClick={handleClick}>
              {Loading ? (
                <img src="./upload.gif" alt="" className="search-icon-gif" />
              ) : (
                <img src="./upload.png" alt="" className="search-icon" />
              )}
            </button>
          </div>
        </div>
        <div className="row2">
          {!startPage && !Loading ? (
            <div className="result-box">
              <Markdown>{searchResults[0].metadata}</Markdown>
            </div>
          ) : (
            <br></br>
          )}
          <ul className="cardList">
            {!startPage && !Loading ? (
              searchResults.map((item, index) => {
                return (
                  <>
                    <li className="card">
                      <div className="card-body">
                        <img
                          src={item.img}
                          alt=""
                          width={"270px"}
                          className="med-image"
                        />
                        <div className="card-bottom">
                          <h1 className="name">{item.name}</h1>
                          <h3 className="brand">Brand : {item.brand}</h3>
                          <h3 className="color">Color : {item.colour}</h3>
                          <h3 className="product">
                            Products : {item.products}
                          </h3>
                          <h3 className="price">Price : ₹{item.price}</h3>
                          <button
                            id={`description-${item.p_id}`}
                            className="description-button"
                            onClick={() => {
                              setOpen(true);
                              setDescription(item.description);
                            }}
                          >
                            Check Description
                          </button>
                        </div>
                      </div>
                    </li>
                  </>
                );
              })
            ) : Loading ? (
              <div className="start-image">
                <img src="./search.png" alt="" />
                <img id="loading" src="./loading.gif" alt="" />
              </div>
            ) : (
              <div className="start-image">
                <img src="./search.png" alt="" />
              </div>
            )}
          </ul>
        </div>
      </div>
      <Modal
        open={open}
        onClose={() => {
          setOpen(false);
        }}
      >
        <Box
          sx={{
            position: "absolute",
            // display: 'flex',
            top: "50%",
            left: "50%",
            transform: "translate(-50%, -50%)",
            width: "50%",
            height: "fit-content",
            bgcolor: "background.paper",
            border: "2px solid #000",
            alignItems: "center",
            justifyContent: "center",
            boxShadow: 24,
            p: 4,
            borderRadius: "15px",
          }}
          dangerouslySetInnerHTML={{ __html: description }}
        ></Box>
      </Modal>
    </>
  );
};

export default Home;
