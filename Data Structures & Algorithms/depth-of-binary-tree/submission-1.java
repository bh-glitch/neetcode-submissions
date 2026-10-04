/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    public int maxDepth(TreeNode root) {
        if(root == null){
            return 0;
        }

        if(root.left==null && root.right==null){ //it has no child
            return 1;
        }
        // if(root.left==null || root.right==null){
            
        // }

        // if(root.left!=null || root.right!=null){ //if it has any child  - could be one left one right or both. 
        // }
        // else{ // it has one child either side
        //     return 1
        // }

        return Math.max(    1+maxDepth(root.left)  ,   1+maxDepth(root.right)   );

        
    }
}
