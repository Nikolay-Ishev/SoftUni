function result(arg) {
    if (arg == `upvote`) {
       return this.upvotes += 1
    } else if (arg == `downvote`) {
       return this.downvotes += 1
    } else if (arg == `score`) {

        //calculate the rating
        let rating
        let sum = this.upvotes + this.downvotes
        if (this.upvotes / (sum) > 0.66) {
            rating = `hot`
        } else if (this.upvotes >= this.downvotes && sum > 100) {
            rating = `controversial`
        } else if (this.upvotes < this.downvotes) {
            rating = `unpopular`
        }
        if (sum < 10 || rating == undefined) {
            rating = `new`
        }

        let balance = this.upvotes - this.downvotes
        //calculate obfuscated numbers and return obfuscated score
        if (sum > 50) {
            let inflateVote = Math.ceil(Math.max(this.upvotes, this.downvotes) * 0.25);
            return [this.upvotes + inflateVote, this.downvotes + inflateVote, balance, rating];
          }

        // return the real score
        return [this.upvotes, this.downvotes, balance, rating]
    }
}


var forumPost = {
    id: '2',
    author: 'gosho',
    content: 'whats up?',
    upvotes: 120,
    downvotes: 30
};
result.call(forumPost, 'upvote');

var answer = result.call(forumPost, 'score');
console.log(answer)
