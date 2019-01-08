#include<iostream>
/*#include<opencv2/core/core.hpp>
#include<opencv2/features2d/features2d.hpp>
#include<opencv2/highgui/highgui.hpp>
*/
using namespace std;
//using namespace cv;

int main(int argc, char ** argv)
{
    if(argc!=3)
    {
        cout<<"Usage:feature_extraction img1 img2"<<endl;
        return 1;
    }
   /* //Load Image
    Mat img1 = imread(argv[1]);
    //Mat img2 = imread(argv[2]);
    cout<<(img1.datalimit - img1.datastart )/1024<<endl; 
    //store keypoint
    vector<KeyPoint> kp1,kp2;
    //store descriptors
    Mat descriptors1, descriptors2;
    getchar();
    Ptr<ORB> orb = ORB::create(500,1.2f,8,31,0,2,ORB::HARRIS_SCORE,31,20);
    //get keypoints
    orb->detect(img1,kp1);
    //orb->detect(img2,kp2);
    getchar();
    //compute the descriptors
    orb->compute(img1,kp1,descriptors1);
    //orb->compute(img2,kp2,descriptors2);
    getchar();
   /* Mat outimg1,outimg2;
    //highlight keypoint on the image 
    drawKeypoints(img1,kp1,outimg1,Scalar::all(-1),DrawMatchesFlags::DEFAULT);
    drawKeypoints(img2,kp2,outimg2,Scalar::all(-1),DrawMatchesFlags::DEFAULT);
    imshow("img1",outimg1);
    imshow("img2",outimg2);


    //use Hamming distance to match 
    vector<DMatch> matches;
    BFMatcher matcher(NORM_HAMMING);//maybe the dist have been normalized
    matcher.match(descriptors1,descriptors2,matches);

    //filter the wrong match(the distance is larger than double min distance)
    //An empirical handling
    double mindist = 1000000;
    for(int i = 0;i!=matches.size();i++)
    {
        double dist = matches[i].distance;
        if(dist < mindist) mindist = dist;
    }

    cout<<"min dist: "<<mindist<<endl;
    if(mindist < 20) mindist = 20;
    vector<DMatch> good_matches;
    for( int i = 0;i!=matches.size();++i)
    {
        if(matches[i].distance <= 2*mindist)
            good_matches.push_back(matches[i]);
    }
    //show the match
    Mat img_match,img_good_match;
    drawMatches(img1,kp1,img2,kp2,matches,img_match);
    drawMatches(img1,kp1,img2,kp2,good_matches,img_good_match);
    imshow("All the matches",img_match);
    imshow("Good matches",img_good_match);*/
  /*  kp1.clear();
    kp2.clear();
    descriptors1.release();
    descriptors2.release();*/
    getchar();
    //waitKey(0);
    return 0;
    

}