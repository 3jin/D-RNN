import pool from './database_pool';
import { convertQuery } from './db_helpers';
import { modelInterpreter } from '../model/model_interpreter';

const getReviewList = async (movieID) => {
  const reviewList = [];
  const rows = await pool.query(
    'SELECT * FROM review WHERE movie_id= ?',
    movieID
  );
  try {
    const attrList = ['comment', 'review_datetime', 'is_friendly'];
    const numResults = rows.length;
    for (let i = 0; i < numResults; i++) {
      reviewList.push(convertQuery(rows[i], attrList));
    }
    return reviewList;
  } catch (err) {
    console.log(err);
    return false;
  }
};

const insertReview = async (movieID, reviewComment) => {
  const dataForInsertion = {
    'comment': reviewComment,
    'review_datetime': new Date(),
    'movie_id': movieID,
  };
  dataForInsertion['is_friendly'] = ((await modelInterpreter(reviewComment, './model/embed.py')) === 'POS');
  try {
    await pool.query(
      'INSERT INTO review SET ?',
      dataForInsertion
    );
  } catch(err) {
    console.log(err);
  }
};

export { getReviewList, insertReview };
