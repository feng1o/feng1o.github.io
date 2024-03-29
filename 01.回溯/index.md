# 01.回溯算法梳理


#[Algorithm 算法](/images/Apple-Devices-Preview.png "algorithm  回溯")
Algorithm - **回溯** learn.

<style>
h6,h5,h4,h3,h2,h1 {
background : lightgray;
}

h6,h5,h4,h3,h2,h1:hover {
color : red;
}





</style>

---

- [summary-backtrack-labuladong](https://labuladong.github.io/algo/di-ling-zh-bfe1b/hui-su-sua-c26da/) && [回溯细分](https://labuladong.github.io/algo/di-san-zha-24031/bao-li-sou-96f79/hui-su-sua-56e11/)
  id:: fa46fb8b-f417-4457-aae7-bcfacfda375d
	- <p class="gray subw  inline_box underline"><span style="color: red;background-color: lightblue;font-weight:bold;font-size:12px;display:inline-block"> 递归回溯区别:</span>回溯也用到递归，但是相比递归多了条件剪纸，结束条件等； 而递归就是回调自身，斐波那契数列为例，不存在发现结果不对倒回去的步骤； 回溯比如一个格子里走出去，走不通了回去继续换个路劲，一般要有个状态记录走过的</p>
	  id:: 9374c530-4426-441e-8048-2362e98c3b7b
	- id:: 63f7088c-681a-4fae-a9f0-3712420bbe3c
	  ```
	  result = []
	  def backtrack(路径, 选择列表):
	      if 满足结束条件:  // 组合的这all都满足，入口就是空也是
	          result.add(路径)
	          return
	      
	      for 选择 in 选择列表:
	  		// 剪枝: 比如同元素的组合 x>start nums[x]=numx[x-1] 跳过
	          做选择
	          backtrack(路径, 选择列表)
	          撤销选择
	  ```
	- id:: 63fc2cd5-d8c2-4e77-8486-b5713111d5bb
	  #+BEGIN_QUERY 
	  {:title [:h5.font-bold.blue.opacity-40"3. query (and BFS (and dalg (not  tpl)) )"]
	  :query (and "回溯" (and "dalg" (not  "tpl")) )
	  :result-transform (fn [result]
	                          (sort-by(  fn [h]
	                                    (get h :db/id 1)  ) > result))
	  :breadcrumb-show?  false
	  :collapsed? true
	  }
	  #+END_QUERY
- leetcode -- backtrace <span class=" bg-green white  subw hblack hover"> [[2023-02-23 Thu]] </span>
  id:: 62360062-8288-4366-a172-6bcfff419cd2
- <html><a  class="alg-2stars"       href=https://leetcode.cn/problems/subsets/description/
  
  
  ><span class="width-55-hide bg-lightgray-del">
  
  78.子集
  
  <span class="hide">dalg</span><span class="hide">hot100</span>
  <span class="gray subw9">
  
  一系列问题-tip-hot100 <span class=" bg-green white  subw hblack hover"> [[2022-11-30 Wed]] </span>
  
  </span></span></a>  <a 
  class="indent1  subw8 blue    width-13-hide                                        " >回溯</a><a 
  class="indent1 subw8 gray    width-18-hide  underline  DarkOrchid  " >回溯</a><a 
  class="indent1 subw gray     width-3-hide  underline  red                  " >1</a>
  </html>
	- <html><a  class="alg-2stars"       href=
	  https://leetcode.cn/problems/subsets/solution/hui-su-suan-fa-by-powcai-5/
	  
	  ><span class="width-55-hide bg-lightgray-del">
	  
	  排列组合子集-汇总
	  
	  <span class="hide">dalg</span>
	  <span class="gray subw9">
	  -tip-
	  </span></span></a>  <a 
	  class="indent1  subw8 blue    width-13-hide                                        " >😁</a><a 
	  class="indent1 subw8 gray    width-18-hide  underline  DarkOrchid  " >😭汇总</a><a 
	  class="indent1 subw gray     width-3-hide  underline  red                  " >0</a>
	  </html>
	- 77. n内的k个数组合     组合和排列区别，在for循环处理，排列all，需要识别visited，组合需去重(start顺序去)
	  90. 子集II   <span class="subw8">有重复、不可复选的组合、排列问题  x=start; num[x]=nums[x-1]忽略</span>
	  40.  组合和等于target   <span class="subw8">有重复、不可复选的组合、排列问题</span>  [[$red]]==组合问题和子集问题等价==  [参考此页](https://labuladong.github.io/algo/di-san-zha-24031/bao-li-sou-96f79/hui-su-sua-56e11/)
	  17. 电话号码的字幕组合 --- 和无重复数字组合一样，从0号开始，扫完进入下一轮，结束就是n到了size
	  22. [括号生成](https://leetcode.cn/problems/generate-parentheses/) 括号生成这个理解 ---
- <html><a  class="alg-2stars"       href=
  
  https://leetcode.cn/problems/permutations/
  
  ><span class="width-55-hide bg-lightgray-del">
  
  46.不同元素的全排列
  
  <span class="hide">dalg</span>
  <span class="gray subw9">
  -tip-
  </span></span></a>  <a 
  class="indent1  subw8 blue    width-13-hide                                        " >回溯</a><a 
  class="indent1 subw8 gray    width-18-hide  underline  DarkOrchid  " >和子集比！</a><a 
  class="indent1 subw gray     width-3-hide  underline  red                  " >1</a>
  </html>
	- 47.  有相同元素的全排列
- <html><a  class="alg-2stars"       href=
  
  https://leetcode.cn/problems/n-queens/
  ><span class="width-55-hide bg-lightgray-del">
  
  5.n皇后问题
  
  <span class="hide">dalg</span>
  <span class="gray subw9">
  -tip-
  </span></span></a>  <a 
  class="indent1  subw8 blue    width-13-hide                                        " >回溯</a><a 
  class="indent1 subw8 gray    width-18-hide  underline  DarkOrchid  " >回溯对比</a><a 
  class="indent1 subw gray     width-3-hide  underline  red                  " >0</a>
  </html>

